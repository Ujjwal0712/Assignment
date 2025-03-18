from langchain_chroma import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv
from modules.data_loader import load_data
from config import CHROMA_DB_PATH

# Load environment variables
load_dotenv()

def create_vector_store():
    
    """Creates a vector store from the scraped data."""
    
    documents = load_data()
    embeddings = MistralAIEmbeddings()
    vector_db = Chroma.from_documents(documents, embeddings, persist_directory=CHROMA_DB_PATH)
    vector_db.persist()
    
    return vector_db
    
def load_vector_store():
    
    """Loads the existing vector store for retrieval."""
    
    embeddings = MistralAIEmbeddings()
    return Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)
    
def get_retriever(vector_db, top_k=5):
    
    """Retrieves top-k relevant travel destinations."""
    
    return vector_db.as_retriever(search_kwargs={"k": top_k})