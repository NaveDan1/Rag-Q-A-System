from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model="nomic-embed-text",  # <--- not llama3
    base_url="http://ollama:11434"
)


def get_embedding(text):
    return embeddings.embed_query(text)
