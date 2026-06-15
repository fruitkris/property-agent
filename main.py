import asyncio
import os
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask, request, jsonify

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION", "")

app = Flask(__name__)
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

@app.route("/get_unit", methods=["GET"])
async def get_unit():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "code required"}), 400
    await client.connect()
    bot = "@PropertyRadarRobot"
    await client.send_message(bot, code)
    await asyncio.sleep(20)
    messages = await client.get_messages(bot, limit=1)
    result = messages[0].text if messages else "Нет ответа"
    return jsonify({"unit": result})

@app.route("/")
def index():
    return "OK"

loop = asyncio.get_event_loop()
loop.run_until_complete(client.connect())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
