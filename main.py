from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
import json
from datetime import datetime
from manager import ConnectionManager
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='templates')

app = FastAPI()

manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Create formatted message
            chat_message = {
                "type": "chat",
                "username": username,
                "message": message_data["message"],
                "timestamp": datetime.now().strftime("%H:%M:%S")
            }
            
            # Broadcast to all connected clients
            await manager.broadcast(json.dumps(chat_message))
            
    except WebSocketDisconnect:
        manager.disconnect(websocket, username)

@app.get("/")
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
