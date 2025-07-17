# Build and store graph using NetworkX
import networkx as nx
from utils.extractor import extract_entities_relations, parse_output
from config import MAX_CHUNKS

def build_graph(chunks):
    G = nx.Graph()
    # use only 600 chunks
    print("Number of chunks: ", len(chunks))
    for chunk in chunks[:MAX_CHUNKS]:
        output = extract_entities_relations(chunk.page_content)
        entities, edges = parse_output(output)
        print("All Sample Entities: ", entities)
        print("\n")      
        print("All Sample Edges: source, target, descriptions", edges)
        for ent in entities:
            G.add_node(ent)
        for src, tgt, desc in edges:
            G.add_edge(src, tgt, description=desc)
    return G
