import json
from langchain.schema import Document
from langchain_experimental.text_splitter import SemanticChunker
from langchain_mistralai import MistralAIEmbeddings

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def load_data(file_path: str):
    
    """Loads scraped travel data from json file"""
    
    with open(file_path, 'r') as f:
        data = json.load(f)
        
    documents= []
    for doc in data:
        content = (
            f"Title: {doc['title']}\n",
            f"Description: {doc['summary']}\n",
            f"Things to do: {doc['article']}\n"
        )
        documents.append(Document(page_content=content))
    
    return documents

def split_text(documents):
    text_splitter = SemanticChunker()
    return text_splitter.split_text(documents)

        
        
    
    