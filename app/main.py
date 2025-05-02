from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.agent import ConversationalAgent

app = FastAPI()
agent = ConversationalAgent()

class ChatInput(BaseModel):
    message: str
    model: str = "Gemini"  

@app.post("/chat")
async def chat_endpoint(input: ChatInput):
    try:
       
        agent.set_model(input.model.lower())  
        reply = await agent.chat(input.message)
        return {"response": reply, "status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))