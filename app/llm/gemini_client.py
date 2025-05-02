import google.generativeai as genai
from app.config import GEMINI_API_KEY

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
       
        self.model_name = 'gemini-1.5-pro-latest'  

    async def generate_response(self, messages):
        try:
            model = genai.GenerativeModel(self.model_name)
            
            chat_history = []
            for msg in messages:
                role = "user" if msg["role"] == "user" else "model"
                chat_history.append({"role": role, "parts": [msg["content"]]})
            
            chat = model.start_chat(history=chat_history[:-1])
            
            response = await chat.send_message_async(chat_history[-1]["parts"][0])
            
            return response.text
        except Exception as e:
            print(f"Gemini API error: {str(e)}")
            return f"Error generating response: {str(e)}"