import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask, request, jsonify
import threading

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION", "")

app = Flask(__name__)
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@app.route("/get_unit", methods=["POST"])
async def get_unit():
    data = request.json
    url = data.get("url")
    await client.connect()
    bot = "@PropertyRadarRobot"
    await client.send_message(bot, url)
    await asyncio.sleep(15)
    messages = await client.get_messages(bot, limit=1)
    result = messages[0].text if messages else "Нет ответа"
    return jsonify({"unit": result})

@app.route("/")
def index():
    return "OK"

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.connect())
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
