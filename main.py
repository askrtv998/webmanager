import os
import requests
from fastapi import FastAPI, Request

app = FastAPI()

# Uses your provided token directly (falls back to environment variables if updated later)
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "9176612733:AAHXgLW4KUr849twomYZPZ2AxSaOHwbOivI")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.get("/")
def home():
    return {"status": "Telegram bot is running smoothly!"}

@app.post("/")
async def handle_webhook(req: Request):
    data = await req.json()
    
    # Check if a message exists in the incoming Telegram update
    if "message" in data:
        message = data["message"]
        chat_id = message["chat"]["id"]
        text = message.get("text", "")
        user_name = message["from"].get("first_name", "User")

        # Basic command handling
        if text == "/start":
            response_text = f"Hello {user_name}! Your flat-structure Vercel Python bot is live. 🚀"
        elif text == "/help":
            response_text = "I am your serverless Telegram bot. Send me any message and I will reply!"
        else:
            response_text = f"Hello {user_name}, you said: '{text}'"

        # Payload to send back to Telegram
        payload = {
            "chat_id": chat_id,
            "text": response_text
        }
        
        # Send the response using Telegram's Bot API
        requests.post(f"{TELEGRAM_API_URL}/sendMessage", json=payload)

    return {"status": "ok"}
