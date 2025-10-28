# 🤖 Chatbot System (Full-Stack AI Assistant)

### 🚀 Overview
This is a full-stack **AI-powered Chatbot** built with:
- **Backend:** FastAPI (Python)
- **Frontend:** Streamlit
- **LLM Integration:** OpenAI GPT models
- **Memory:** Custom vector memory store (`memory_store.py`)
- **RAG (Retrieval-Augmented Generation):** Implemented via `rag_agent.py`

It allows interactive, contextual chat with persistent memory and knowledge retrieval.

---

### 🧩 Tech Stack
| Layer | Technology |
|--------|-------------|
| Backend | 🐍 FastAPI, Uvicorn |
| Frontend | 🎨 Streamlit |
| AI/ML | 🧠 OpenAI API, RAG |
| Database/Memory | Custom In-Memory Vector Store |
| Tools | Git, VS Code, Python 3.13 |

---

### 🧠 Folder Structure

chatbot/
├── backend/
│ ├── app.py # FastAPI backend
│ ├── rag_agent.py # RAG pipeline logic
│ ├── memory_store.py # In-memory vector database
│ └── app_test_root.py # API test
├── frontend/
│ └── streamlit_app.py # Frontend UI
└── README.md


---

### ⚙️ Installation & Run

#### 1️⃣ Clone Repository
```bash
git clone https://github.com/Shank312/chatbot.git
cd chatbot

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Backend (FastAPI)
python -m uvicorn backend.app:app --reload --host 127.0.0.1 --port 8000

✅ Server live at: http://127.0.0.1:8000

5️⃣ Run Frontend (Streamlit)
streamlit run frontend/streamlit_app.py


🧩 Example Use

Start the FastAPI backend

Open the Streamlit app

Ask contextual questions — the system retrieves knowledge & responds intelligently


🧰 Future Improvements

Add vector database (FAISS or ChromaDB)

JWT auth for multi-user support

LangChain integration

UI/UX enhancements with Tailwind + Streamlit components


👤 Author

Shankar Kumar
AI/ML Engineer | Full-Stack Developer
🌐 GitHub • 💼 LinkedIn


⭐ Contribute

Pull requests are welcome! If you like this project, please star ⭐ the repo.

