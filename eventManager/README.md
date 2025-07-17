# EventManager: Multi-Agent Event Planning System

## Overview
EventManager is an AI-driven, multi-agent workflow system for automating event planning and management. It leverages modular agents, a stateful workflow graph, and LLM-powered tools to streamline the process of planning events such as parties, conferences, and more.

## Features
- **Automated Event Planning:** From initial request to finalization, the system handles all steps.
- **Modular Agents:** Each step (planning, venue selection, vendor management, scheduling, budgeting, approval) is handled by a dedicated agent.
- **Human-in-the-Loop:** Human approval steps for critical decisions (e.g., venue and vendor selection).
- **Dynamic Workflow:** Uses a state graph to manage conditional flows and retries.
- **Extensible:** Easily add new agents or steps to the workflow.
- **Data-Driven:** Uses real CSV data for venues and vendors.

## Architecture
- **Python**: Main language.
- **Pydantic**: For state schema and validation.
- **LangGraph**: For workflow orchestration as a stateful graph.
- **LangChain**: For LLM-powered agent logic.
- **FAISS**: For vector-based retrieval from CSV data.
- **Virtual Environment**: For dependency isolation.

## Directory Structure
```
eventManager/
  allagents/         # Agent node implementations (planner, vendor_manager, etc.)
  event_data/        # CSV data for venues and vendors
  tools/             # Tool wrappers for agents (venue_tool, vendor_tool, etc.)
  graph.py           # Workflow graph definition
  main.py            # Entry point for running the system
  requirements.txt   # Python dependencies
```

## Setup
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```


## Usage
1. **Run the main program:**
   ```bash
   python main.py
   ```
2. **Follow the prompts:**
   - Enter your event request (e.g., "Wedding in Bangalore for 200 guests with dinner and music").
   - The system will guide you through planning, venue selection, vendor selection, scheduling, budgeting, and approvals.
   - Human approval is requested for key decisions.

## How It Works
- **State Management:**
  - The event state is managed using a Pydantic model, updated at each step.
- **Agents:**
  - Each agent is a function that takes the current state, performs its logic, and returns an updated state.
- **Workflow Graph:**
  - The flow is defined in `graph.py` using LangGraph, with conditional edges for approvals and retries.
- **Data:**
  - Venue and vendor data are loaded from CSV files and used for recommendations.
- **Human Approval:**
  - At certain steps, the system pauses for human input to approve or reject options.

## Example Event Request
```
Product launch in Mumbai for 150 guests with AV setup, catering, and live music.
```

## Extending the System
- **Add a new agent:**
  - Create a new Python file in `allagents/` with your agent logic.
  - Register the agent in `graph.py` and add it to the workflow.
- **Add new data:**
  - Update or add CSV files in `event_data/`.
- **Change workflow:**
  - Edit `graph.py` to modify the flow or add conditional logic.


## Acknowledgements
- [LangChain](https://github.com/langchain-ai/langchain)
- [LangGraph](https://github.com/langchain-ai/langgraph)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Pydantic](https://github.com/pydantic/pydantic) 