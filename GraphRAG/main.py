# main file for answering queries
from utils import chunker, graph_builder, community, query_engine
import json
import pickle
import os

#GRAPH_FILE = "./outputs/graph.gpickle"
SUMMARY_FILE = "./outputs/summaries.json"

def main():
    summaries = {} # all summaries
    # If summary file present then just read else build from scratch
    if os.path.exists(SUMMARY_FILE):
        print("Summary file already exists. Loading...")
        with open(SUMMARY_FILE, "r") as f:
            summaries = json.load(f)
    print("summary: ", summaries)
    # For first time creating from chunking to summaries 
    # or When new data added to ./data/, use hashlib for compare the new hashes to the old ones -> save hases in json file
    if not summaries:
        # ............. Indexing Time ............. ##
        print("Loading and chunking documents...")
        chunks = chunker.load_and_split_documents()
    
        print("Building Knowledge Graph")
        G = graph_builder.build_graph(chunks)
        # Save graph if needed
        #with open("outputs/graph.gpickle", "wb") as f:
         #pickle.dump(G, f)
        
        print("Detecting Communities")
        G = community.detect_communities(G)
    
        print("Summarizing Communities (for first time)")
        summaries = community.summarize_community(G)
        with open(SUMMARY_FILE, "w") as f:
            json.dump(summaries, f, indent=2)

    # ............. Query Time ............. ##
    print("Answering query...")
    query = input("Enter your query: ")
    answer = query_engine.answer_query(query, summaries)
    print("\n Final Answer:\n", answer)

if __name__ == "__main__":
    main()
