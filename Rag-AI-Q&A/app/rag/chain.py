# chain.py

import os
from datetime import datetime
from pymongo import MongoClient
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
from app.database.chroma_client import vectorstore  # ✅ Use your existing vectorstore

# 🔹 Setup LLM
ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://ollama:11434")
llm = OllamaLLM(model="llama3.2", base_url=ollama_base_url)

# 🔹 Setup MongoDB logging
mongo_url = os.getenv("MONGO_URL", "mongodb://mongodb:27017/")
client = MongoClient(mongo_url)
db = client["llm_logs"]
collection = db["queries"]

# 🔹 Build the RAG chain
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    return_source_documents=True
)

def query_llm(question: str):
    # ✅ Pass input using the correct key
    result = rag_chain.invoke({"query": question})

    answer = result["result"]
    source_docs = result.get("source_documents", [])
    citations = [doc.metadata.get("source", "unknown") for doc in source_docs]

    # 📝 Log the interaction
    collection.insert_one({
        "question": question,
        "answer": answer,
        "citations": citations,
        "timestamp": datetime.now()
    })

    return answer, citations
