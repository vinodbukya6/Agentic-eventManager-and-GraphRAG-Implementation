# Import libraries
from langgraph.graph import StateGraph, END # LangGrap
from pydantic import BaseModel # State schema validation and management
# Warnings
import warnings
warnings.filterwarnings("ignore")

# Define the state of the event
class EventState(BaseModel):
    event_request: str = "" # user input
    event_plan: str = "" # planner
    venue_options: dict = {} # venue finder
    selected_venue: str = "" # user prefernce venue selection
    venue_results: str = ""
    vendor_results: str = "" # vendor manager
    vendor_approved: bool = False # human approval
    event_schedule: str = "" # scheduler
    budget_results: str = "" # budget analyst
    final_plan: str = "" #final event plan    
    budget_summary: str = "" # budget analyst
    event_location: str = "" # location
    event_categories: list = [] # required setup, categories
    special_requirements: str = "" # any special resquirements
    
# Import agent nodes
def import_nodes():
    from allagents.planner import planner_node
    from allagents.vendor_manager import vendor_node
    from allagents.venue_finder import venue_node
    from allagents.scheduler import scheduler_node
    from allagents.budget_analyst import budget_node
    from allagents.human_approval import human_approval_node_venue, human_approval_node_vendor
    from allagents.finalizer import finalizer_node
    return {
        "planner": planner_node,
        "vendor_manager": vendor_node,
        "venue_finder": venue_node,
        "scheduler": scheduler_node,
        "budget_analyst": budget_node,
        "human_approval_venue": human_approval_node_venue,
        "human_approval_vendor": human_approval_node_vendor,
        "finalizer": finalizer_node
    }
# If vendor is approved, go to scheduler, otherwise go to vendor manager

    
def route_after_vendor(state):
    if getattr(state, "vendor_approved", False):
        return "scheduler"
    else:
        return "vendor_manager" # retry

def build_event_graph():
    nodes = import_nodes()
    graph = StateGraph(EventState)

    # Add all nodes
    for name, func in nodes.items():
        graph.add_node(name, func)

    # Set entry
    graph.set_entry_point("planner")

    # Define flow
    graph.add_edge("planner", "venue_finder")
    graph.add_edge("venue_finder", "human_approval_venue")
    graph.add_edge("human_approval_venue", "vendor_manager")
    graph.add_edge("vendor_manager", "human_approval_vendor")
    graph.add_conditional_edges("human_approval_vendor", route_after_vendor)
    graph.add_edge("scheduler", "budget_analyst")
    graph.add_edge("budget_analyst", "finalizer")
    graph.add_edge("finalizer", END)

    return graph.compile()

if __name__ == "__main__":
    print("\n Welcome to the Multi-Agent Event Planner!")
    user_prompt = input("\nPlease describe your event (e.g., Product launch in Bangalore for 200 guests with dinner, music, and AV setup):\n\n")

    graph = build_event_graph()
    final_state = graph.invoke({"event_request": user_prompt})

    print("\n Final Event Plan Summary:\n")
    print(final_state.get("final_plan", "No final summary was generated."))




