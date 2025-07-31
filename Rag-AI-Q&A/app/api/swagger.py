from flasgger import Swagger

def setup_swagger(app):
    template = {
        "swagger": "2.0",
        "info": {
            "title": "RAG-based Academic Q&A System API",
            "description": "API for uploading academic papers and querying them using RAG with Ollama and ChromaDB.",
            "version": "1.0.0"
        },
        "definitions": {
            "QueryRequest": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string"
                    }
                },
                "required": ["question"]
            },
            "QueryResponse": {
                "type": "object",
                "properties": {
                    "answer": {
                        "type": "string"
                    },
                    "citations": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                }
            }
        }
    }

    return Swagger(app, template=template)
