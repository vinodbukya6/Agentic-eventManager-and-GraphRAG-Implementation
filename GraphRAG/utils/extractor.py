# Entity and Relationship extraction
import re
import ast
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from config import OPENAI_MODEL, TEMPERATURE
from dotenv import load_dotenv
load_dotenv()
# load model
llm = ChatOpenAI(temperature=TEMPERATURE, model_name=OPENAI_MODEL)

# Relation ship extraction
def extract_entities_relations(text):
    entity_prompt = PromptTemplate(
        input_variables=["text"],
        template="""
        You are an expert information extraction assistant.
        Given the following text, identify and extract:
        1. All key named entities (such as people, organizations, locations, concepts, etc.).
        2. All explicit and implicit relationships between these entities.
        Please respond in the following structured format:
        Entities: [Entity1, Entity2, ...]
        Relations:
        - EntityA -> EntityB: <type or description of relationship>
        - EntityB -> EntityC: <type or description of relationship>
        
        If no entities or relations are found, state "None".
        Text:
        {text}
        """
        )
    return llm.invoke(entity_prompt.format(text=text))

# Extract entities
def safe_parse_entities(raw_line: str):
    line_cleaned = raw_line.replace("Entities:", "").strip()
    if not line_cleaned:
        return []

    try:
        # Try safe eval first
        return ast.literal_eval(line_cleaned)
    except:
        # Fallback: parse as comma-separated string
        items = [item.strip().strip('"').strip("'") for item in line_cleaned.strip("[]").split(',')]
        # Wrap all in quotes to make them proper strings
        return [str(item) for item in items if item]
    
# LLM Ouput formatting
def parse_output(output):
    entities = []
    edges = []
    #lines = output.splitlines()
    lines = output.content.splitlines()
    for line in lines:
        if line.startswith("Entities:"):
            entities = safe_parse_entities(line)

        elif "->" in line:
            match = re.match(r"- (.+?) -> (.+?): (.+)", line)
            if match:
                src, tgt, desc = match.groups()
                edges.append((src.strip(), tgt.strip(), desc.strip()))
    #
    #if entities and edges:
        #print("Sample Entities: ", entities[0],", Edges: ", edges[0])
        #print("Number of  Entities: ",len(entities), ", Number of Edges: ", len(edges))
    return entities, edges
