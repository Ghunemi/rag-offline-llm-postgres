# 🧠 RAG Offline LLM with PostgreSQL

This project is a lightweight, fully offline Retrieval-Augmented Generation (RAG) system that uses:
- 🐘 PostgreSQL as a structured knowledge base
- 🦙 `llama-cpp-python` to run a quantized local LLM (like Mistral)
- 🧠 LangChain to orchestrate natural language → SQL → answer pipeline

---

## 🚀 Features

- Ask natural questions like:
  - "Which employees work in the IT department?"
  - "List the top 5 clients."
  - "How many hours did each employee work on Project X?"
- Automatically generates and executes PostgreSQL queries
- Runs completely offline (no OpenAI or cloud APIs required)

---

## 🧩 Project Structure

```bash
rag_offline_pg_llm/
├── main.py              # CLI entrypoint
├── model.py             # Llama-cpp wrapper for local model
├── rag_pipeline.py      # Full RAG logic using LangChain
├── setup_database.py    # Script to generate schema and fake data
├── requirements.txt     # Python dependencies
├── README.md            # You’re reading this
└── models/
    └── mistral-7b-instruct-v0.2.Q4_K_M.gguf  # (Download manually or script)

🛠️ Setup Instructions
1. Clone the repo
    git clone https://github.com/your-username/rag-offline-pg-llm.git
    cd rag-offline-pg-llm

2. Install dependencies
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

3. Set up PostgreSQL
    Ensure PostgreSQL is installed and running on your machine. Create a database named rag_test.
        createdb rag_test
    Then run:
        python setup_database.py

4. Download a Quantized Model
Download Mistral-7B-Instruct (GGUF) from TheBloke on Hugging Face:

Recommended file:
    mistral-7b-instruct-v0.2.Q4_K_M.gguf


💡 Example Queries
What is the total salary paid to employees?

List me 3 projects.

Who are the highest-paid employees?

Which clients are in the banking industry?

🤝 Contributions
Open a pull request or issue if you’d like to improve this project or add a web UI.