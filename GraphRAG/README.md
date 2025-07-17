# GraphRAG Pipeline

GraphRAG Pipeline is a document processing pipeline that extracts text from PDF files, splits them into manageable chunks, and prepares them for downstream tasks such as retrieval-augmented generation (RAG) or knowledge graph construction.


## Features
- Extracts text from PDF documents in the `data/` directory
- Splits documents into overlapping chunks for efficient processing
- Modular utilities for chunking, extraction, graph building, and querying
- Text Chunks → Entities & Relationships
- Entities & Relationships → Knowledge Graph
- Knowledge Graph → Graph Communities
- Community Summaries → Community Answers
- Global Sensemaking Question Generation

## Directory Structure
```
GraphRAG/
  ├── config.py                # Configuration variables (chunk size, paths, etc.)
  ├── data/                    # Directory for input PDF files
  ├── main.py                  # Main file 
  ├── requirements.txt         # Python dependencies
  └── utils/
      ├── chunker.py           # PDF loading and chunking logic
      ├── community.py         # Community detection utilities
      ├── extractor.py         # Information extraction utilities
      ├── graph_builder.py     # Graph construction logic
      └── query_engine.py      # Querying and retrieval logic
```


## Setup
- Python 3.8+
   ```bash
   pip install -r requirements.txt
   ```

## Usage
run:
```bash
python3 main.py
```

This will generate resopnse to the input query