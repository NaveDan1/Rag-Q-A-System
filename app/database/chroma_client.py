from langchain_chroma import Chroma
from langchain.docstore.document import Document
from app.utils.embeddings import embeddings

vectorstore = Chroma(
    collection_name="pdf_chunks",
    embedding_function=embeddings,
    persist_directory="/tmp/chroma_db"
)


def add_document_chunks(chunks, metadata):
    docs = [Document(page_content=chunk, metadata={"source": metadata}) for chunk in chunks]
    vectorstore.add_documents(docs)


def retrieve_relevant_chunks(query, top_k=3):
    docs = vectorstore.similarity_search(query, k=top_k)
    return [doc.page_content for doc in docs]


def load_vectorstore():
    global vectorstore
    vectorstore = Chroma(
        collection_name="pdf_chunks",
        embedding_function=embeddings,
        persist_directory="/tmp/chroma_db"
    )
