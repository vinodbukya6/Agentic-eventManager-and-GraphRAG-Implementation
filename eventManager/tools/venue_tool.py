# tools/venue_tool.py

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

import csv
from langchain.schema import Document

def get_venue_tool():
    docs = []
    with open("event_data/venues.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # You can customize the content/metadata as needed
            content = ", ".join([f"{k}: {v}" for k, v in row.items()])
            docs.append(Document(page_content=content, metadata=row))
    # Now, docs is a list of row-wise documents
    vectordb = FAISS.from_documents(docs, OpenAIEmbeddings())
    retriever = vectordb.as_retriever()
    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        retriever=retriever,
        return_source_documents=False
    )
    return qa



