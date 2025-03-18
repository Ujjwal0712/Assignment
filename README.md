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

1️. Retrieval-Augmented Generation (RAG)

- Instead of relying solely on the LLM’s internal knowledge, the system retrieves context from a vector database, improving accuracy and relevance.

2. Modular Structure

- rag_pipeline.py: Contains functions for initializing the RAG pipeline and generating answers.
- vector_store.py: Handles vector database loading.
- main.py: Provides the CLI interface for user interaction.
    
3. Incorporation of Web Scraping:
   
- Ensures real-time and updated travel information instead of relying solely on static datasets.

### How to Run 🚀

Step 1: Install Dependencies

    pip install langchain_mistralai langchain_core langchain_community scrapy
       
Step 2: Run the Chatbot

    python main.py

Step 3: Ask Questions!

Example:

    🌍 Welcome to AI Travel Consultant! 🌍

     Ask me about travel destinations (or type 'exit' to quit): Plan me a 3 day itinerary for Udaipur

     AI Travel Consultant Recommendation: 
     
     Sure, I'd be happy to help you plan your 3-day itinerary for Udaipur, also known as the "City of Lakes". Here's a suggested itinerary:
     
     Day 1:
     * Morning: Start your day by visiting the City Palace, a magnificent palace complex that offers a glimpse into the rich history and culture of Udaipur. Explore the many courtyards, gardens, and museums within the        palace complex.
     * Afternoon: After lunch, head to Jagmandir Island, located in the middle of Lake Pichola. You can take a boat ride to the island and explore the beautiful gardens and palaces.
     * Evening: Enjoy a sunset view of Lake Pichola from the Ambrai Ghat. There are many restaurants nearby where you can enjoy a delicious dinner while taking in the stunning views.
     
     Day 2:
     * Morning: Visit the Saheliyon Ki Bari, a beautiful garden that was built for the queen and her friends. The garden features fountains, lotus pools, and marble elephants.
     * Afternoon: After lunch, head to the Monsoon Palace, which offers panoramic views of the city and the surrounding hills. The palace was built by Maharana Sajjan Singh in the 19th century and is a great place to         learn about the history of Udaipur.
     * Evening: Explore the local markets and try some street food. The Hathi Pol Bazaar is a great place to shop for souvenirs, while the Bapu Bazaar is known for its delicious street food.
     
     Day 3:
     * Morning: Visit the Eklingji Temple, which is located about 22 kilometers from Udaipur. The temple is dedicated to Lord Shiva and is a popular pilgrimage site.
     * Afternoon: After lunch, head to the Sajjangarh Wildlife Sanctuary, which is home to a variety of wildlife, including leopards, panthers, and deer. You can take a safari through the sanctuary and enjoy the              beautiful scenery.
     * Evening: End your trip with a relaxing boat ride on Lake Fateh Sagar. The lake is surrounded by hills and offers a peaceful atmosphere to unwind and reflect on your trip.
     
     I hope this itinerary helps you make the most of your 3 days in Udaipur!


👨‍💻 Built with LangChain & MistralAI for smarter travel recommendations! ✈️

