This Repository contains:
# 1. EventManager: Multi-Agent Event Planning System

# Overview
EventManager is an AI-driven, multi-agent workflow system for automating event planning and management. It leverages modular agents, a stateful workflow graph, and LLM-powered tools to streamline the process of planning events such as parties, conferences, and more.

# Features
1. Automated Event Planning: From initial request to finalization, the system handles all steps.
2. Modular Agents: Each step (planning, venue selection, vendor management, scheduling, budgeting, approval) is handled by a dedicated agent.
3. Human-in-the-Loop: Human approval steps for critical decisions (e.g., venue and vendor selection).
4. Dynamic Workflow: Uses a state graph to manage conditional flows and retries.
5. Extensible: Easily add new agents or steps to the workflow.
6. Data-Driven: Uses real CSV data for venues and vendors.

# 2. GraphRAG Pipeline Learning Implementation

GraphRAG Pipeline is a document processing pipeline that extracts text from PDF files, splits them into manageable chunks, and prepares them for downstream tasks such as retrieval-augmented generation (RAG) or knowledge graph construction.

# Features
Extracts text from PDF documents in the data/ directory
1. Splits documents into overlapping chunks for efficient processing
2. Modular utilities for chunking, extraction, graph building, and querying
3. Text Chunks → Entities & Relationships
4. Entities & Relationships → Knowledge Graph
5. Knowledge Graph → Graph Communities
6. Community Summaries → Community Answers
7. Global Sensemaking Question Generation


# 3. RAG Pipelines Leanrings Document

Traditional vector RAG,  Graph RAG and Agentic RAG summary of each methodoliges.

For endt to end explanation please check in respective directories.


