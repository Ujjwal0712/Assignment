# AI Travel Consultant

### Overview

The AI Travel Consultant is a conversational AI system that provides travel recommendations based on user queries. It leverages a Retrieval-Augmented Generation (RAG) pipeline to enhance responses by retrieving relevant information from a vector database before generating an answer. The chatbot maintains memory for a more engaging and context-aware conversation.

The system follows a Retrieval-Augmented Generation (RAG) approach:
- Web Scraping: Extracts real-time travel data such as weather, popular destinations, and current travel restrictions.
- Retrieve Relevant Information: Uses a ChromaDB vector store to retrieve contextual information.
- Generate Responses: Passes the retrieved context and query to MistralAI for natural language generation.

### Tools & Technologies:

- LangChain → Framework for building LLM applications
-  Scrapy: For extracting travel-related data from websites.
- MistralAI → Language model for response generation
- ChromaDB → Vector database for document retrieval


### Key Design Decisions

1️⃣ Retrieval-Augmented Generation (RAG)

Instead of relying solely on the LLM’s internal knowledge, the system retrieves context from a vector database, improving accuracy and relevance.

2️⃣ Modular Structure

rag_pipeline.py: Contains functions for initializing the RAG pipeline and generating answers.

vector_store.py: Handles vector database loading.

main.py: Provides the CLI interface for user interaction.

How to Run 🚀

Step 1: Install Dependencies

       
Step 2: Run the Chatbot

      python main.py

Step 3: Ask Questions!

Example:

🌍 Welcome to AI Travel Consultant! 🌍

Ask me about travel destinations (or type 'exit' to quit): Where should I travel in Europe?
🌍 AI Travel Consultant Recommendation:
I recommend visiting Italy for its rich history and amazing cuisine!

Future Improvements

Web & Mobile UI → Deploy as a web app.

Fine-tuned Retrieval → Improve document chunking & ranking.

Multi-modal Support → Add image-based travel suggestions.

👨‍💻 Built with LangChain & MistralAI for smarter travel recommendations! ✈️

