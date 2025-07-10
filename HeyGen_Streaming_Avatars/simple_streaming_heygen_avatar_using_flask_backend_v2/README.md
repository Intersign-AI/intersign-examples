# Enhanced Streaming HeyGen Avatar (Python-Centric)

`simple_streaming_heygen_avatar_using_flask_backend_v2`

An implementation with enhanced security and structured backend handling of HeyGen's Streaming Avatar API.

### Features

- Secure API key handling
- Backend API route management
- WebRTC streaming
- Comprehensive error handling
- Real-time avatar interactions

### Prerequisites

- Python 3.7+
- Flask
- python-dotenv
- requests
- HeyGen API Key/Trial Token

### Quick Start

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install flask python-dotenv requests
   ```
3. Create `.env`:
   ```
   HEYGEN_API_KEY=your_api_key_here
   ```
4. Run:
   ```bash
   python app.py
   ```
5. Visit `http://localhost:5000`

### Project Structure

```
simple_streaming_heygen_avatar_using_flask_backend_v2/
├── .env             # Environment variables
├── app.py           # Flask application
└── templates/
    └── index.html   # Frontend UI
```

### Security Features

- Secure API key storage
- Backend API routing
- Protected endpoints
- Error handling

### API Routes

- `/api/session/new`: Create session
- `/api/session/start`: Start streaming
- `/api/session/ice`: Handle ICE
- `/api/session/task`: Send text
- `/api/session/stop`: End session

### Implementation Notes

- Uses [Raw WebRTC (v1)](https://docs.heygen.com/docs/streaming-api-integration-raw-webrtc-approach) approach
- Backend-focused API handling
- Recommended for further development use
- Enhanced security measures
