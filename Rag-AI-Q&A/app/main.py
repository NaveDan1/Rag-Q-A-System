from flask import Flask
from app.api.endpoints import api_blueprint
from app.api.swagger import setup_swagger
from app.database.chroma_client import load_vectorstore  # ⬅️ Import your function

app = Flask(__name__)

setup_swagger(app)                 # Swagger setup
load_vectorstore()                # ⬅️ ✅ Load Chroma vectorstore into memory
app.register_blueprint(api_blueprint)  # Register all API routes

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
