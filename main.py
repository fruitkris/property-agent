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
    bot = "@PropertyRadarR
