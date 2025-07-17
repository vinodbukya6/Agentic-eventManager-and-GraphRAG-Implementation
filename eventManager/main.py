# import graph
from main_graph import build_event_graph

if __name__ == "__main__":
    print("\n🎉 Welcome to the Multi-Agent Event Planner! 🎉")
    user_prompt = input("\nPlease describe your event (e.g., Product launch in Bangalore for 200 guests with dinner, music, and AV setup):\n\n")

    graph = build_event_graph()
    final_state = graph.invoke({"event_request": user_prompt})

    print("\n✅ Final Event Plan Summary:\n")
    print(final_state.get("final_plan", "No final summary was generated."))
