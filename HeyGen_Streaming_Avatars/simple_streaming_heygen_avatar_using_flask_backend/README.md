
## Simple Streaming HeyGen Avatar (JavaScript-Centric)

`simple_streaming_heygen_avatar_using_flask_backend`

A lightweight implementation of HeyGen's Streaming Avatar API using Flask backend with JavaScript-heavy frontend.

### Features

- Direct WebRTC streaming implementation
- Frontend-focused API calls
- Real-time avatar interactions
- Simple session management
- Avatar selection system

### Prerequisites

- Python 3.7+
- Flask
- HeyGen API Key/Trial Token
- Basic WebRTC knowledge

### Quick Start

1. Clone the repository
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Add your HeyGen API key to `index.html`
4. Run:
   ```bash
   python app.py
   ```
5. Visit `http://localhost:5000`

### Project Structure

```
simple_streaming_heygen_avatar_using_flask_backend/
├── app.py           # Flask server
└── templates/
    └── index.html   # Main application logic and UI
```

### Implementation Notes

- Uses [Raw WebRTC (v1)](https://docs.heygen.com/docs/streaming-api-integration-raw-webrtc-approach) approach
- Direct API calls from frontend
- Minimal backend involvement
- Suitable for prototypes and learning JS based WebRTC
