# HeyGen Real-time Interactive Avatar Implementations

This folder contains three different implementations of HeyGen's Streaming Avatar API integration, demonstrating various approaches to building real-time interactive avatar applications:

### Available Implementations

1. **HeyGen's Official NextJS Implementation** (`InteractiveAvatarNextJSDemo/`)

   - Original source: [HeyGen Official Demo](https://github.com/HeyGen-Official/InteractiveAvatarNextJSDemo/tree/realtime-alpha-demo)
   - Customized for real-time text repeating use case
   - Built with NextJS for a modern, scalable architecture
2. **Simple Flask Backend with JavaScript Frontend** (`simple_streaming_heygen_avatar_using_flask_backend/`)

   - Lightweight implementation
   - Most API calls handled in frontend JavaScript
   - Minimal Flask backend
3. **Enhanced Flask Backend Implementation** (`simple_streaming_heygen_avatar_using_flask_backend_v2/`)

   - More structured implementation
   - API calls handled by Flask backend for enhanced security features
   - Recommended for further python based backend development

## About HeyGen Streaming API

HeyGen's Streaming API enables seamless integration of dynamic Interactive Avatars into applications for immersive user experiences. The API supports:

- Real-time avatar interactions
- Virtual assistants
- Training simulations
- Low-latency communication using WebRTC

#### Key Features

- **Low Latency**: Real-time communication using WebRTC
- **Cross-Browser Compatibility**: Works across modern browsers
- **Data Security**: Secure communication channels
- **Scalability**: Built for enterprise-grade applications

### Getting Started with HeyGen API

#### Obtaining API Access

1. Get your API Key or Trial Token:

   - Login to HeyGen and visit: [API Settings](https://app.heygen.com/settings?nav=API)
   - New users receive 10 free API Credits
   - Use trial token if you don't have an enterprise API token
2. Available Avatars:

   - Public Avatars: Available in Interactive Avatar section
   - Private Avatars: Must be upgraded to Interactive Avatars
   - Supported types: Finetune Instant Avatars and Studio Avatars
   - Note: Photo Avatars are not compatible

#### Documentation Resources

- [Official API Documentation](https://docs.heygen.com/reference/heygen-interactive-avatar-realtime-api)
- [Streaming API Guide](https://docs.heygen.com/docs/streaming-api)
- [Raw WebRTC Integration Guide](https://docs.heygen.com/docs/streaming-api-integration-raw-webrtc-approach)
- [Interactive Avatar Guide](https://help.heygen.com/en/articles/9182113-interactive-avatar-101-your-ultimate-guide)
- [API Pricing](https://www.heygen.com/api-pricing)

### Technical Implementation Details

#### API Endpoints (v1)

1. `POST /v1/streaming.new`: Create new streaming session
2. `POST /v1/streaming.start`: Start WebRTC session
3. `POST /v1/streaming.ice`: Handle ICE candidates
4. `POST /v1/streaming.task`: Send text to avatar
5. `POST /v1/streaming.stop`: End session

#### Prerequisites

- HeyGen API Token
- Understanding of WebRTC concepts
- Web server capability
- Basic knowledge of chosen framework (NextJS or Flask)

---
