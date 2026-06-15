import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask, request, jsonify

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION", "")

app = Flask(__name__)

@app.route("/")
def index():
   return "OK"

@app.route("/get_unit")
def get_unit():
   code = request.args.get("code")
   if not code:
       return jsonify({"error": "code required"}), 400
   
   async def run():
       client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
       await client.connect()
       await client.send_message("me", "тест " + code)
       await asyncio.sleep(5)
       await client.disconnect()
       return "sent"
   
   result = asyncio.run(run())
   return jsonify({"status": result})

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 8000))
   app.run(host="0.0.0.0", port=port)
