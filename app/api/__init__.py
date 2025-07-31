from flask_restx import Api

api = Api(
    version='1.0',
    title='RAG-based Academic Q&A System API',
    description='API for uploading academic papers and querying them using RAG with Ollama and ChromaDB.',
    doc='/swagger'
)
