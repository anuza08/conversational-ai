# 🤖 Conversational AI Chatbot

A versatile chatbot interface supporting multiple LLM backends (Gemini, Claude) with seamless model switching. Built with Python, FastAPI, and Gradio.

### Working Demo
https://github.com/user-attachments/assets/945ba9ce-2c5c-499b-b193-7c96dd3ed489


## 🚀 Features

- Switch between **Gemini** and **Claude** models on-the-fly
- Beautiful Gradio web interface
- FastAPI backend for scalable deployments
- Conversation history tracking
- Easy API integration

## ⚙️ Setup

### Prerequisites
- Python 3.9+
- [Poetry](https://python-poetry.org/) (recommended)
- API keys:
  - [Google Gemini API Key](https://ai.google.dev/)
  - [Anthropic Claude API Key](https://console.anthropic.com/) (optional)

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/conversational-ai.git
cd conversational-ai

# Install dependencies (using Poetry)
poetry install

# Or with pip
pip install -r requirements.txt

```
### Configuration
1. Create .env file:

```
# Required
GEMINI_API_KEY=your_google_api_key

# Optional (for Claude support)
CLAUDE_API_KEY=your_anthropic_key
LLM_PROVIDER=gemini  # default
```

### 🖥️ Usage
Running the Application

```
# Start FastAPI backend
uvicorn app.main:app --reload

# In another terminal, start Gradio UI
python frontend/gradio_ui.py
```

Access the UI at http://localhost:7860


### 🔄 LLM Switching Guide
<h3>Via UI</h3>
1. Use the dropdown in the web interface
2. Select either "Gemini" or "Claude"
3. Continue chatting - the model will change immediately

![Demo GIF](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDhyNnRlMGJ6dW1rY3B2eWZ4Z2N0Y3VtYzN6bmRlZ2Z1Z2Z1ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT5LMHxhOfscxPfIfm/giphy.gif)

### Via API
```
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello", "model":"claude"}'
```
