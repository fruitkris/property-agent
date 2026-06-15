import asyncio
import os
from telethon import TelegramClient, events

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
SESSION = os.environ.get("SESSION")

client = TelegramClient("session", API_ID, API_HASH)

async def get_unit_number(url: str) -> str:
    await client.start()
    bot = "@PropertyRadarRobot"
    await client.send_message(bot, url)
    await asyncio.sleep(10)
    messages = await client.get_messages(bot, limit=1)
    return messages[0].text if messages else "Нет ответа"

if __name__ == "__main__":
    asyncio.run(get_unit_number("test"))
