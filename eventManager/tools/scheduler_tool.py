# imports
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

def get_scheduler_tool():
    prompt = PromptTemplate(
        input_variables=["input"],
        template="""
        You are a scheduling assistant. Create a detailed schedule based on the following event plan:
        {input}

        Include timings for setup, main sessions, meals, entertainment, and cleanup.
        """
    )
    chain = LLMChain(llm=ChatOpenAI(temperature=0), prompt=prompt)
    return chain
