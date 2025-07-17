# tools/budget_tool.py

from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

def get_budget_tool():
    prompt = PromptTemplate(
        input_variables=["input"],
        template="""
        You're a budget analyst. Estimate the total event cost in rupees from given this context:
        {input}

        Break it down by:
        - Venue cost
        - Vendor costs (catering, music, etc.)
        - Add 10% contingency

        Output a detailed breakdown and total.
        """
    )
    chain = LLMChain(llm=ChatOpenAI(temperature=0), prompt=prompt)
    return chain
