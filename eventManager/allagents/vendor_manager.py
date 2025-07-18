# import from tools
from tools.vendor_tool import get_vendor_tool

vendor_tool = get_vendor_tool()

def vendor_node(state):
    event_plan = state.event_plan
    location = state.event_location
    categories = state.event_categories

    query = (
        f"Select the top 1 vendor in each of the following categories: {', '.join(categories)}.\n"
        f"Event Plan: {event_plan}\n"
        f"Special Requirements: {state.special_requirements}\n"
        f"Only select vendors located in {location}. Return concise summaries."
    )

    #print("vendor query: ", query)
    result = vendor_tool.run(query)
    print("Vendor tool: " ,result)
    return {**state.model_dump(),"vendor_results": result}
