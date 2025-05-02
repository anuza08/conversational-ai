from app.llm_router import route_request

class ConversationalAgent:
    def __init__(self):
        self.history = []
        self.current_model = "gemini"  

    def set_model(self, model_name: str):
        """Switch between Gemini and Claude"""
        valid_models = ["gemini", "claude"]
        if model_name.lower() not in valid_models:
            raise ValueError(f"Invalid model. Choose from {valid_models}")
        self.current_model = model_name.lower()

    async def chat(self, user_input: str) -> str:
        try:
            self.history.append({"role": "user", "content": user_input})
            
            response = await route_request(self.history, self.current_model)
            
            if not isinstance(response, str):
                response = str(response)
                
            self.history.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            print(f"Error in chat: {str(e)}")
            return f"Error: {str(e)}"