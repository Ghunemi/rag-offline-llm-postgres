from rag_pipeline import build_rag_chain

def main():
    print("\U0001F517 Starting RAG system...")
    chain = build_rag_chain()
    print("✅ Ready. Ask your questions below (type 'exit' to quit):\n")

    while True:
        question = input("You: ")
        if question.lower() in {"exit", "quit"}:
            break
        try:
            answer = chain.invoke({"question": question})
            print(f"\n\U0001F9E0 Answer: {answer}\n")
        except Exception as e:
            print(f"\n[Error] {str(e)}\n")

if __name__ == "__main__":
    main()