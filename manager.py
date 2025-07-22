from fastapi.websockets import WebSocket
from typing import List
from datetime import datetime
import json

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.users: dict = {}
    
    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append(websocket)
        self.users[websocket] = username
        
        # Notify others that user joined
        join_message = {
            "type": "system",
            "message": f"{username} joined the chat",
            "timestamp": datetime.now().strftime("%H:%M:%S")
        }
        await self.broadcast(json.dumps(join_message), exclude=websocket)
    
    def disconnect(self, websocket: WebSocket, username: str):
        if websocket in self.active_connections:
            # username = self.users.get(websocket, "Unknown")
            self.active_connections.remove(websocket)
            del self.users[websocket]
            
            # Notify others that user left
            leave_message = {
                "type": "system", 
                "message": f"{username} left the chat",
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
            # Broadcast to remaining connections
            import asyncio
            for connection in self.active_connections:
                try:
                    asyncio.create_task(connection.send_text(json.dumps(leave_message)))
                except:
                    pass

    async def broadcast(self, message: str, exclude: WebSocket = None):

        connections_copy = self.active_connections.copy()

        for connection in connections_copy:
            if connection != exclude:
                try:
                    await connection.send_text(message)
                except:
                    # Remove broken connections
                    if connection in self.active_connections:
                        self.active_connections.remove(connection)
                        if connection in self.users:
                            del self.users[connection]