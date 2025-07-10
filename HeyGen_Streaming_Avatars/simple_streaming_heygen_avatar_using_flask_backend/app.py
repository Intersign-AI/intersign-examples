from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    """
    Render the main page that includes the HTML & JavaScript 
    for the Raw WebRTC (v1) HeyGen demo.
    """
    # If you prefer, you can inject your API key here from an environment variable:
    # api_key = os.getenv("HEYGEN_API_KEY", "your_api_key")
    # Then pass it to the template via render_template(..., api_key=api_key)

    return render_template("index.html")

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True, host="0.0.0.0", port=5000)
