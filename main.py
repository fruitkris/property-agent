import os
import threading
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask, request, jsonify
import asyncio

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION", "")

app = Flask(__name__)
loop = asyncio.new_event_loop()
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH, loop=loop)

def start_client():
    loop.run_until_complete(client.connect())
    loop.run_forever()

threading.Thread(target=start_client, daemon=True).start()

@app.route("/get_unit", methods=["GET"])
def get_unit():
    code = request.args.get("code")
    if not code:
        return jsonify({"error": "code required"}), 400
    
    async def task():
        await client.send
