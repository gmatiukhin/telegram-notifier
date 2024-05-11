from flask import Flask, request
import telegram
import os

app = Flask("telegram-notifier")
bot = telegram.Bot(os.environ["BOT_TOKEN"])
USER_CHAT_ID = os.environ["USER_CHAT_ID"]

@app.route("/health")
def health():
    return "Alive"

@app.route("/send", methods=["POST"])
async def send():
    message = request.json["text"]
    async with bot:
        await bot.send_message(text=message, chat_id=USER_CHAT_ID)
    return {"status": "success"}, 200
