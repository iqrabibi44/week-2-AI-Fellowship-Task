import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def ai_response(user_input, persona):
    system_prompts = {
        "Professional Assistant": "You are a professional, formal AI assistant. Give clear and structured answers.",
        "Creative Companion": "You are an imaginative, artistic AI. Respond with creative and inspiring language.",
        "Casual Friend": "You are a friendly, informal AI friend. Respond casually with emojis and slang when appropriate."
    }

    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"{system_prompts[persona]}\nUser: {user_input}"

    response = model.generate_content(prompt)

    return response.text.strip()
