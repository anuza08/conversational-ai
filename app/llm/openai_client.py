import httpx
from app.config import OPENAI_API_KEY

class OpenAIClient:
    async def generate_response(self, messages):
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": messages,
        }
        async with httpx.AsyncClient() as client:
            response = await client.post("https://api.openai.com/v1/chat/completions", json=payload, headers=headers)
        return response.json()["choices"][0]["message"]["content"]