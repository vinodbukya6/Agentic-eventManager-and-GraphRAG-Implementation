import json
def human_approval_node_venue(state):
    venue_options = state.venue_options
    print("Top 3 venue options:")
    for k, v in venue_options.items():
        #print(f"[{k}] {v['Venue Name']} - Capacity: {v['Capacity']}, Cost: ₹{v['Cost']}, Rating: {v['Ratings']}")
        print(f"[{k}] {v.get('Venue Name', 'N/A')} - Capacity: {v.get('Capacity', 'N/A')}, Cost: ₹{v.get('Cost', 'N/A')}, Rating: {v.get('Rating', 'N/A')}")
        #Venue Name,City,Capacity,Cost,Features,Ratings,Availability

    choice = input("Select a venue by number (1-3): ").strip()
    #selected_venue = venue_options.get(choice, venue_options["1"])  # Default to 1 if invalid
    selected_venue = venue_options.get(choice) if venue_options else "" # default is empty string
    return {**state.model_dump(), "venue_results": json.dumps(selected_venue)}

def human_approval_node_vendor(state):
    print("\n VENDOR SELECTION REQUIRES HUMAN APPROVAL")
    print("Suggested Vendors:\n")
    #print(state.get("vendor_results", "No vendors found."))
    print(getattr(state, "vendor_results", "No vendors found."))
    approval = input("\nDo you approve these vendors? (yes/no): ").strip().lower()
    #return {**state, "vendor_approved": approval == "yes"}
    return {**state.model_dump(), "vendor_approved": approval == "yes"}
