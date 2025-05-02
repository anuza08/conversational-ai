import anthropic
from app.config import CLAUDE_API_KEY

class ClaudeClient:
    def __init__(self):
        self.client = anthropic.AsyncAnthropic(api_key=CLAUDE_API_KEY)

    async def generate_response(self, messages):
        try:
          
            claude_messages = []
            for msg in messages:
                role = "user" if msg["role"] == "user" else "assistant"
                claude_messages.append({"role": role, "content": msg["content"]})
           
            response = await self.client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1000,
                messages=claude_messages
            )
            
            return response.content[0].text
        except Exception as e:
            print(f"Claude API error: {str(e)}")
            return f"Error generating response: {str(e)}"