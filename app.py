from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS to allow external requests

@app.route("/")
def home():
    return "Flask API is running on Hugging Face!"

@app.route("/recommend", methods=["GET"])
def recommend_anime():
    anime_name = request.args.get("anime_name")
    if not anime_name:
        return jsonify({"error": "No anime name provided"}), 400
    
    recommendations = ["Attack on Titan", "Death Note", "One Punch Man", "Tokyo Ghoul", "Code Geass"]
    
    return jsonify({"anime_name": anime_name, "recommendations": recommendations})

# Ensure Gunicorn finds 'app' variable
if __name__ == "__main__":
    print("🔥 API is starting...")  # Debugging print statement
    app.run(host="0.0.0.0", port=7860)

app = app  # Force Gunicorn to detect the app
