# Community detection and summarization
import networkx as nx
import community as community_louvain
from collections import defaultdict
from langchain.chat_models import ChatOpenAI
from config import OPENAI_MODEL, TEMPERATURE
from dotenv import load_dotenv
load_dotenv()

# Load model
llm = ChatOpenAI(temperature=TEMPERATURE, model_name=OPENAI_MODEL)

def detect_communities(G):
    partition = community_louvain.best_partition(G)
    for node, cid in partition.items():
        G.nodes[node]['community'] = cid
    return G

# Summary
def summarize_community(G):
    community_nodes = defaultdict(list)
    for node, data in G.nodes(data=True):
        community_nodes[data['community']].append(node)

    summaries = {}
    for cid, nodes in community_nodes.items():
        info = []
        for n in nodes:
            edges = list(G.edges(n, data=True))
            for e in edges:
                info.append(f"{e[0]} -> {e[1]}: {e[2].get('description', '')}")

        joined = "\n".join(set(info))
        prompt = f"Summarize the following relationships:\n{joined}"
        summaries[cid] = llm.predict(prompt)
    return summaries






