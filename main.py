from modules.rag_pipeline import generate_answer

def main():
    print("🌍 Welcome to AI Travel Consultant! 🌍")
    
    
    while True:
        query = input("\nAsk me about travel destinations (or type 'exit' to quit): ").strip()
        
        if query.lower() == 'exit':
            print("\n👋 Thanks for using AI Travel Consultant! Safe travels! ✈️")
            break
        
        if not query:
            print("⚠️ Please enter a valid question.")
            continue
        
        response = generate_answer(query)
        print("\n🌍 AI Travel Consultant Recommendation:\n", response)


if __name__ == "__main__":
    main()