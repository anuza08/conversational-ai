import gradio as gr
import requests

def chat_fn(message: str, history: list, model_choice: str):
    try:
        if model_choice == "Claude":
            raise ValueError("Claude API requires credits. Switch to Gemini or add billing.")
        # Gemini fallback
        response = requests.post(
            "http://localhost:8000/chat",
            json={"message": message, "model": "gemini"}
        )
        return response.json().get("response")
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

with gr.Blocks(theme=gr.themes.Soft()) as app:
    gr.Markdown("## 🤖 **AI Chatbot with Model Switching**", elem_id="header", css=".gr-markdown h2 {color: #4C9EF1; text-align: center;}")

   
    model_selector = gr.Dropdown(
        choices=["Gemini", "Claude"],
        value="Gemini",
        label="Select AI Model",
        style={"background-color": "#F1F5F8", "border-radius": "8px", "padding": "10px"}
    )
    
    
    chatbot = gr.Chatbot(
        height=400,
        bubble_full_width=False,
        avatar_images=("👤", "🤖"), 
        style={"border-radius": "15px", "background-color": "#F9F9FB"}
    )
    
    
    input_box = gr.Textbox(
        placeholder="Type your message here...",
        label="Your Message",
        show_label=False,
        container=False,
        autofocus=True,
        style={"background-color": "#F1F5F8", "border-radius": "8px", "padding": "10px", "width": "100%"}
    )
    
    
    with gr.Row():
        send_btn = gr.Button("Send", variant="primary", size="lg", style={
            "background-color": "#4C9EF1", 
            "color": "white", 
            "border-radius": "50px", 
            "padding": "12px 24px",
            "font-weight": "bold",
            "transition": "transform 0.3s ease, background-color 0.3s ease", 
            "cursor": "pointer",
        })
        
        send_btn.hover(style={
            "background-color": "#3378A8",  
            "transform": "scale(1.1)" 
        })

        clear_btn = gr.ClearButton([input_box, chatbot], style={
            "background-color": "#E0E4E7", 
            "border-radius": "50px", 
            "color": "#333", 
            "padding": "12px 24px",
            "font-weight": "bold",
            "cursor": "pointer",
            "transition": "transform 0.3s ease, background-color 0.3s ease"
        })

        clear_btn.hover(style={
            "background-color": "#D1D7DB", 
            "transform": "scale(1.1)" 
        })
    
   
    def respond(message, chat_history, model):
       
        messages = chat_history + [{"role": "user", "content": message}]
        response = chat_fn(message, messages, model)
        return "", chat_history + [(message, response)]
    
   
    input_box.submit(
        respond,
        [input_box, chatbot, model_selector],
        [input_box, chatbot]
    )
    
    send_btn.click(
        respond,
        [input_box, chatbot, model_selector],
        [input_box, chatbot]
    )

app.launch()
