# import from tools
import ast
from tools.venue_tool import get_venue_tool

venue_tool = get_venue_tool()

def venue_node(state):
    query = (
        f"Find suitable venues based on this event plan: {state.event_plan}. "
        f"Only consider venues that are currently 'Available'. "
        f"Only consider venues in the city {state.event_location}. "
        f"Return the top 2 venues as a dictionary with keys 1 and 2, where each value is the venue's details. "
        f"Example output: {{'1': {{'Venue Name': 'ABC Hall', 'Capacity': 300, 'Cost': 150000, 'Features': 'Garden, AC', 'Rating': 4.7, 'Availability': 'Available'}}, '2': {{...}}}}. "
        f"Only return valid Python dictionary output."
    )

    result = venue_tool.run(query)
    if isinstance(result, str):
        try:
            result = ast.literal_eval(result)
            if not isinstance(result, dict):
                raise ValueError("Not a dictionary")
        except Exception as e:
            print("Failed to parse venue response:", e)
            result = {}

    print("✅ Parsed Venue Options:", result)
    return {**state.model_dump(), "venue_options": result}
