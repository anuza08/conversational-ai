from app.config import LLM_PROVIDER
from app.llm.claude_client import ClaudeClient
from app.llm.gemini_client import GeminiClient

async def route_request(messages, model_choice=None):
    provider = model_choice if model_choice else LLM_PROVIDER
    
    if provider == "claude":
        client = ClaudeClient()
    else:  # Default to Gemini
        client = GeminiClient()
        
    return await client.generate_response(messages)