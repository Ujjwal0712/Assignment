from langchain_mistralai import ChatMistralAI
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

from modules.vector_store import load_vector_store


def initialize_rag():
    """Initializes the RAG model."""
    vector_db = load_vector_store()
    retriever = vector_db.as_retriever()
    
    # Initialize the LLM
    llm = ChatMistralAI()
    
    # Define the prompt template
    prompt_template = ChatPromptTemplate.from_template(
        "Answer the question based on the context:\n\nContext: {context}\n\nQuestion: {question}"
    )
    
    # Create the RAG chain
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | prompt_template  # Pass the context and question to the prompt template
        | llm  # Pass the formatted prompt to the LLM
        | StrOutputParser()  # Parse the LLM output into a string
    )
    
    return rag_chain


def generate_answer(question):
    """Generates an answer to the input question."""
    rag_chain = initialize_rag()
    return rag_chain.invoke(question)