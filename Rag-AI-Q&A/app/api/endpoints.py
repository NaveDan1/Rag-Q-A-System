# app/api/endpoints.py
from flask import Blueprint, request, jsonify
from flasgger import swag_from
from app.utils.pdf_processor import extract_text_from_pdf, chunk_text
from app.rag.chain import query_llm
from app.database.chroma_client import add_document_chunks, retrieve_relevant_chunks
from app.models.models import QueryRequest

api_blueprint = Blueprint("api", __name__)


@api_blueprint.route("/papers", methods=["POST"])
@swag_from({
    'tags': ['PDF Upload'],
    'parameters': [
        {
            'name': 'files',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'Upload one or more PDF files'
        }
    ],
    'responses': {
        200: {
            'description': 'Upload successful',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {'type': 'string'},
                    'chunks': {'type': 'integer'}
                }
            }
        }
    }
})
def upload_papers():
    files = request.files.getlist("files")
    all_chunks = []
    for file in files:
        filename = file.filename
        text = extract_text_from_pdf(file)
        chunks = chunk_text(text)
        add_document_chunks(chunks, filename)
        all_chunks.extend(chunks)
    return jsonify({"status": "success", "chunks": len(all_chunks)})


@api_blueprint.route("/query", methods=["POST"])
@swag_from({
    'tags': ['Query'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                '$ref': '#/definitions/QueryRequest'
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Query successful',
            'schema': {
                '$ref': '#/definitions/QueryResponse'
            }
        }
    }
})
def handle_query():
    data = request.get_json()
    validated = QueryRequest(**data)

    # 🔍 Retrieve relevant chunks from Chroma
    relevant_chunks = retrieve_relevant_chunks(validated.question)

    # 🧠 Generate LLM response
    context = "\n".join(relevant_chunks)
    answer, sources = query_llm(validated.question)


    # 📝 Return both answer and chunks for transparency
    return jsonify({
        "answer": answer,
        "citations": sources,
        "chunks": relevant_chunks  # optional, remove if you don't want to expose this
    })
