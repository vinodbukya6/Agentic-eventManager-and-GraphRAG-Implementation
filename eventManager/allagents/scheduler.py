# agents/scheduler.py

from tools.scheduler_tool import get_scheduler_tool

scheduler_tool = get_scheduler_tool()

def scheduler_node(state):
    query = f"Create a proposed event schedule based on this plan: {state['event_plan']}"
    result = scheduler_tool.run(query)
    return {**state, "event_schedule": result}
# agents/scheduler.py

from tools.scheduler_tool import get_scheduler_tool

scheduler_tool = get_scheduler_tool()

def scheduler_node(state):
    query = f"Create a proposed event schedule based on this plan: {state.event_plan}"
    result = scheduler_tool.run(query)
    #return {**state, "event_schedule": result}
    return {**state.model_dump(), "event_schedule": result}
