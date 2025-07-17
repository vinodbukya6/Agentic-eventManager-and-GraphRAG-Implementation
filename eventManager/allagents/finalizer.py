# agents/finalizer.py

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI


def finalizer_node(state):
    prompt = PromptTemplate(
        input_variables=["event_plan", "venue", "vendors", "schedule", "budget"],
        template="""
        Prepare a final event summary using the following details:

        Event Plan:
        {event_plan}

        Venue:
        {venue}

        Vendors:
        {vendors}

        Schedule:
        {schedule}

        Budget:
        {budget}

        Return the full formatted event summary.
        """
    )
    chain = LLMChain(llm=ChatOpenAI(temperature=0), prompt=prompt)
    result = chain.run(
        event_plan=state.event_plan,
        venue=state.venue_results,
        vendors=state.vendor_results,
        schedule=state.event_schedule,
        budget=state.budget_summary
    )
    #return {**state, "final_plan": result}
    return {**state.model_dump(), "final_plan": result}

