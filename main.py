import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from flask import Flask, request, jsonify

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION", "")
SESSION2 = os.environ.get("SESSION2", "")

app = Flask(__name__)

@app.route("/")
def index():
   return "OK"

@app.route("/get_unit")
def get_unit():
   code = request.args.get("code")
   if not code:
       return jsonify({"error": "code required"}), 400
   
   session = SESSION2 if SESSION2 else SESSION
   
   async def run():
       client = TelegramClient(StringSession(session), API_ID, API_HASH)
       await client.connect()
       await client.send_message("@PropertyRadarRobot", code)
       await asyncio.sleep(30)
       msgs = await client.get_messages("@PropertyRadarRobot", limit=1)
       result = msgs[0].text if msgs else "no response"
       await client.disconnect()
       return result
   
   result = asyncio.run(run())
   return jsonify({"unit": result})

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 8000))
   app.run(host="0.0.0.0", port=port)
