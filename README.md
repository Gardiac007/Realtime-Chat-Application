# Real-time Chat Application 💬

A real-time chat application built with WebSockets and FastAPI, enabling multiple users to communicate in chat rooms with live messaging capabilities.

## Features ✨

- **Real-time Messaging**: Send and receive messages instantly using WebSocket connections
- **Multi-user Support**: Multiple users can join and participate in chat rooms simultaneously  
- **Username Display**: Messages show the sender's username for easy identification
- **Connection Status**: Real-time notifications when users connect or disconnect
- **Minimal UI**: Clean and responsive frontend built with HTML and JavaScript

## Technology Stack 🛠️

**Backend:**
- Python
- FastAPI (Web framework)
- WebSockets (Real-time communication)

**Frontend:**
- HTML
- JavaScript
- CSS (for styling)

## API Endpoints 🔌

- `WS /ws/{client_id}` - WebSocket endpoint for real-time communication

## WebSocket Events 📡

The application handles the following WebSocket events:

- **User Connection**: Broadcasts when a new user joins
- **User Disconnection**: Notifies when a user leaves
- **Message Broadcasting**: Sends messages to all connected clients
- **Username Registration**: Associates usernames with WebSocket connections
