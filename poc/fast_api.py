from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Any, Dict

app = FastAPI()

# -----------------------------
# Define the request body schema
# -----------------------------
class ChatRequest(BaseModel):
    message: str # Expecting a JSON body with a single field 'message' of type string

# ------------------------------
# Define the response body schema
# ------------------------------
class ChatResponse(BaseModel):
    response: str # # The API will return a single field 'response' of type string

# -------------------------------------
# Define the POST /api/chat endpoint
# -------------------------------------
@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # Extract the message sent by the user from the request body
    user_message = request.message

    # Generate a simple bot response by echoing the user's message
    bot_response = f"Ankit said: {user_message}"

    # Return the response in the format defined by ChatResponse model
    return {"response": bot_response}

