# app.py
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
import requests

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Constants
HEYGEN_API_URL = "https://api.heygen.com"
API_KEY = os.getenv("HEYGEN_API_KEY")

# Available avatars
AVATARS = [
    {
        "avatar_id": "Tyler-incasualsuit-20220721",
        "name": "Tyler in Casual Suit"
    },
    {
        "avatar_id": "Anna_public_3_20240108",
        "name": "Anna in Brown T-shirt"
    },
    {
        "avatar_id": "Susan_public_2_20240328",
        "name": "Susan in Black Shirt"
    }
]

def make_heygen_request(endpoint, data=None):
    """Helper function to make requests to HeyGen API"""
    headers = {
        "Content-Type": "application/json",
        "X-Api-Key": API_KEY
    }
    
    url = f"{HEYGEN_API_URL}{endpoint}"
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@app.route("/")
def index():
    """Render the main page with avatar options"""
    return render_template("index.html", avatars=AVATARS)

@app.route("/api/avatars", methods=["GET"])
def get_avatars():
    """Return list of available avatars"""
    return jsonify(AVATARS)

@app.route("/api/session/new", methods=["POST"])
def create_session():
    """Create a new streaming session"""
    try:
        request_data = request.json
        avatar_id = request_data.get('avatar_id', 'Anna_public_3_20240108')  # Default to Anna if not specified
        
        data = {
            "quality": "high",
            "avatar_name": avatar_id,
            "voice": {"voice_id": ""}
        }
        
        response = make_heygen_request("/v1/streaming.new", data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Rest of the routes remain the same...
@app.route("/api/session/start", methods=["POST"])
def start_session():
    """Start the streaming session"""
    try:
        data = request.json
        response = make_heygen_request("/v1/streaming.start", data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/session/ice", methods=["POST"])
def handle_ice():
    """Handle ICE candidates"""
    try:
        data = request.json
        response = make_heygen_request("/v1/streaming.ice", data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/session/task", methods=["POST"])
def send_task():
    """Send text to avatar"""
    try:
        data = request.json
        response = make_heygen_request("/v1/streaming.task", data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/session/stop", methods=["POST"])
def stop_session():
    """Stop the streaming session"""
    try:
        data = request.json
        response = make_heygen_request("/v1/streaming.stop", data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)