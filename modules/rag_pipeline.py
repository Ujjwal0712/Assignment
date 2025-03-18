from langchain_mistralai import ChatMistralAI
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


from modules.vector_store import load_vector_store


def initialize_rag():
    """Initializes the RAG model with conversational memory."""
    vector_db = load_vector_store()
    retriever = vector_db.as_retriever()  # Limit retrieval
    
    llm = ChatMistralAI()  # Enable streaming for faster responses
    

    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "Answer the question based on the context and chat history:\n\nContext: {context}\n\nQuestion: {question}"),
        ("human", "{question}"),
    ])
    
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
        | prompt_template
        | llm
        | StrOutputParser()
    )
    
    return rag_chain

def generate_answer(question):
    """Generates an answer asynchronously."""
    rag_chain = initialize_rag()
    response = rag_chain.invoke({"question": question})
   
    return response
