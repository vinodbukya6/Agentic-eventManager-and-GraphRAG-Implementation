# import libraries
import re
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

# List of cities
CITIES = ["Hyderabad", "Chennai", "Bangalore", "Mumbai", "Delhi"]
# Location present in the user input or not
def extract_location(text):
    for city in CITIES:
        if city.lower() in text.lower():
            return city
    return None

# Categories
CATEGORIES = ["Catering", "Photography", "Lighting", "Stage Setup",
              "Entertainment", "Decoration", "Audio", "Staffing", "Transport"]

# Extract categories from user input like requirements 
def extract_categories(event_plan):
    categories = ["Catering", "Stage Setup"] # Default values
    plan_lower = event_plan.lower()
    for cat in CATEGORIES:
        if cat.lower() in plan_lower:
            categories.append(cat)
    return categories

# Planner agent node
def planner_node(state):
    event_request = state.event_request # Event request input
    location = extract_location(event_request) # extract location
    categories = extract_categories(event_request) # extract categories

    if not location:
        print("Location not detected in event request. Please choose a city from the below list.")
        print("Available cities: \n", "\n".join(CITIES))
        location = input().strip().capitalize() # User input 
        if location not in CITIES:
            print("Invalid city. Defaulting to Hyderabad.")
            location = "Hyderabad"
            
        # Append to request for context
        event_request += f" in {location}"

    prompt = PromptTemplate(
        input_variables=["event_request","categories"],
        template="""
        You are a Professional Event Planner. Given the event request: "{event_request}",
        create a structured plan that includes:
        - Event type
        - Location
        - Guest count
        - Venue preferences 
        - Budget constraints in indian rupees
        - Category needs from {categories}
        - Special notes or constraints
        """
    )
    chain = LLMChain(llm=ChatOpenAI(temperature=0), prompt=prompt)
    result = chain.run(event_request=event_request, categories=categories)
    print("Planner: ", result)
    return {**state.dict(), "event_plan": result,
            "event_location": location,
            "event_categories": categories} 



