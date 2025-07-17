# agents/budget_analyst.py

from tools.budget_tool import get_budget_tool

budget_tool = get_budget_tool()

def budget_node(state):
    query = f"""Estimate total cost based on the following: 
    Plan: {state.event_plan}
    Vendors: {state.vendor_results}
    Venue: {state.venue_results}"""
    result = budget_tool.run(query)
    #return {**state, "budget_summary": result}
    return {**state.model_dump(), "budget_summary": result}

