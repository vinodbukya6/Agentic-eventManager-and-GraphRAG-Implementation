# main file for answering queries
from utils import chunker, graph_builder, community, query_engine
import json
import pickle
import os

SUMMARY_FILE = "./outputs/summaries.json"
#GRAPH_FILE = "./outputs/graph.gpickle"
OUTPUTS_DIR = "./outputs"

if not os.path.exists(OUTPUTS_DIR):
    os.makedirs(OUTPUTS_DIR)

def load_summaries():
    if os.path.exists(SUMMARY_FILE):
        print("Summary file present")
        try:
            with open(SUMMARY_FILE, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading summaries: {e}")
    return {}

def save_summaries(summaries):
    try:
        with open(SUMMARY_FILE, "w") as f:
            json.dump(summaries, f, indent=2)
    except Exception as e:
        print(f"Error saving summaries: {e}")

def build_index():
    print("Loading and chunking documents")
    chunks = chunker.load_and_split_documents()

    print("Building Knowledge Graph...")
    G = graph_builder.build_graph(chunks)
    # Optionally save the graph
    # with open(GRAPH_FILE, "wb") as f:
    #     pickle.dump(G, f)

    print("Detecting Communities")
    G = community.detect_communities(G)

    print("Summarizing Communities (for first time)")
    summaries = community.summarize_community(G)
    save_summaries(summaries) # save summary file
    return summaries

def main():
    # .......... Indexing Time ............. ###
    summaries = load_summaries()
    if not summaries:
        print("Building Indexing from scratch")
        summaries = build_index()
    if summaries:
        # For multiple Q&A 
        while True:
            try:
                # ............. Query Time ............. ##
                query = input("Enter your query: ")
                print("Answering query ")
                answer = query_engine.answer_query(query, summaries)
                print("\n Final Answer:\n", answer)
            except KeyboardInterrupt:
                print("Exiting")
                break

if __name__ == "__main__":
    main()



