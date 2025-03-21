from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from anime_recommender import get_recommendations  # Import your full recommendation code

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route("/")
def home():
    return "Flask API is running on Render!"

@app.route("/recommend", methods=["GET"])
def recommend_anime():
    anime_name = request.args.get("anime_name")
    if not anime_name:
        return jsonify({"error": "No anime name provided"}), 400
    
    # Call your real recommendation function
    recommended_anime = get_recommendations(anime_name)

    return jsonify({"anime_name": anime_name, "recommendations": recommended_anime})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860, debug=True)
