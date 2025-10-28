

# chatbot/backend/app.py
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .rag_agent import generate_response
from .memory_store import session_store

app = FastAPI(title="Chatbot API", version="1.0")

# Enable CORS for frontend (Streamlit/React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # In production, restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(message: dict):
    """
    HTTP endpoint for chat messages.
    Returns a complete response (non-streaming).
    """
    session_id = message.get("session_id", "default")
    user_msg = message["message"]

    # Save user message in memory
    session_store.add_message(session_id, "user", user_msg)

    # Get bot reply (could be str or generator)
    reply = generate_response(session_id, user_msg)

    # If it's a generator (in case generate_response accidentally yields), consume it
    if hasattr(reply, "__iter__") and not isinstance(reply, (str, bytes)):
        reply = "".join(reply)

    # Save bot reply
    session_store.add_message(session_id, "bot", reply)

    # Return JSON response
    return {"reply": reply}


@app.websocket("/ws/chat")
async def websocket_chat(ws: WebSocket):
    """
    WebSocket endpoint for real-time streaming responses.
    Streams token-by-token reply to the frontend.
    """
    await ws.accept()
    session_id = "default"

    try:
        while True:
            # Wait for user message
            user_msg = await ws.receive_text()
            session_store.add_message(session_id, "user", user_msg)

            # Stream the bot reply token by token
            for token in generate_response(session_id, user_msg, stream=True):
                await ws.send_text(token)

            # Indicate message complete
            await ws.send_text("[END]")

    except Exception as e:
        print(f"[WebSocket closed] {e}")
        await ws.close()
