
# 🎓 RAG-Based Academic Q&A System

An intelligent, AI-powered system for asking questions about uploaded academic documents (PDFs) using Retrieval-Augmented Generation (RAG) and modern language models.

> Upload your papers, ask natural questions, and get context-aware answers using ChromaDB + LLAMA3.

---

## 🚀 Key Features

- 📄 Upload academic PDF files  
- ❓ Ask free-text questions like: *"What is the main argument of this paper?"*  
- 🧠 Answers generated with LLAMA3 via Ollama  
- 🔍 Context retrieved from your actual documents using ChromaDB  
- 🌐 Swagger UI for ease-of-use (no coding required)  

---

## 🙌 Don’t Know How to Code?

👉 **One-click run via GitHub Codespaces:**

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?repo=YourUsername/Nave-AI&machine=basicLinux&devcontainer_path=.devcontainer/devcontainer.json)

> Once Codespace is open, the server will automatically run using:

```bash
docker-compose up --build
```
Then go to:  
📎 `http://localhost:5000/apidocs`

---

## 🧩 Tech Stack

| Component        | Technology               |
|------------------|---------------------------|
| 🌐 Backend        | Python + Flask            |
| 📚 Vector Store   | ChromaDB                  |
| 🔤 Embeddings     | Nomic Embed Text          |
| 🤖 LLM            | Ollama (LLAMA3)           |
| ☁️ Database       | MongoDB                   |
| 📦 Deployment     | Docker + Docker Compose   |
| 🚦 API UI         | Swagger via Flasgger      |

---

## 📁 Folder Structure

```bash
app/
├── api/
│   ├── __init__.py
│   └── endpoints.py
├── database/
│   ├── __init__.py
│   ├── chroma_client.py
│   └── mongo_client.py
├── rag/
│   ├── __init__.py
│   ├── chain.py
│   ├── output_parser.py
│   └── prompt_templates.py
├── utils/
│   ├── __init__.py
│   └── pdf_processor.py
├── config.py
├── main.py
├── embeddings.py
└── logging.py
```

---

## ⚙️ Local Setup (Developers)


# Step 1: Build and run the app
```bash
docker-compose up --build
```


# Step 2: Open the Swagger UI
http://localhost:5000/apidocs
```

---

## 💡 How to Use via Swagger

1. 📤 Upload a PDF file  
   `POST /upload`

2. ❓ Ask a question  
   `GET /query?question=What are the main findings?`

3. 📘 Get an AI-generated answer and citations

**Example Response:**

```json
{
  "answer": "The paper argues that...",
  "citations": ["page_3", "page_8"]
}
```

---

## 🔧 Future Improvements

- 🖥️ Web-based GUI (non-Swagger) for non-technical users  
- 📄 Support for DOCX and TXT formats  
- 🧠 Chat history and memory  
- 😊 Sentiment & tone detection  
- ⬆️ Drag & drop PDF interface

---

## 🤝 Contributing

Feel free to open issues, submit pull requests, or suggest features.  
Let’s make this project even better — together!

---


