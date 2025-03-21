from flask import Flask, request, jsonify
from flask_cors import CORS
import gdown
import joblib
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Google Drive file ID of the model
MODEL_ID = "1ndGqM4O8szaAvy4HoXDgRM2R53O5Z8nS"  # Replace with your actual ID
MODEL_PATH = "recommendation_model.pkl"

# Download model from Google Drive if not already downloaded
if not os.path.exists(MODEL_PATH):
    print("📥 Downloading model from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?id={MODEL_ID}", MODEL_PATH, quiet=False)
    print("✅ Model downloaded successfully!")

# Load the model
model = joblib.load(MODEL_PATH)
print("✅ Model loaded successfully!")

@app.route("/")
def home():
    return "Flask API is running on Render!"

@app.route("/recommend", methods=["GET"])
def recommend_anime():
    anime_name = request.args.get("anime_name")
    if not anime_name:
        return jsonify({"error": "No anime name provided"}), 400

    # Use the loaded model to get recommendations
    recommended_anime = model.predict(anime_name)  # Ensure your model has this function

    return jsonify({"anime_name": anime_name, "recommendations": recommended_anime})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)
