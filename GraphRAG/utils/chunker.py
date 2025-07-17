# Document loading and chunking
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
import os
from config import CHUNK_SIZE, CHUNK_OVERLAP, DOCUMENTS_PATH

def load_and_split_documents():
    pdf_dir = DOCUMENTS_PATH
    pdf_files = [f for f in os.listdir(pdf_dir) if f.lower().endswith('.pdf')]
    docs = []
    for pdf_file in pdf_files:
        loader = PyPDFLoader(os.path.join(pdf_dir, pdf_file))
        docs.extend(loader.load())
    docs = docs[:10]  # lets reduce no. docs 
    print("Doc Size: ", len(docs)) 
    # splitter
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.split_documents(docs)

if __name__ == "__main__":
    out = load_and_split_documents()
    print(len(out))
    print(out[0])
