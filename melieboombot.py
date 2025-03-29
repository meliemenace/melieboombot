import asyncio
import logging
from telegram import Bot

# Replace with your actual Telegram Bot Token
BOT_TOKEN = "7627360725:AAEyuSjrl74NPOgiGd2iswSfwikptlG5j38"
CHAT_ID = "1041102787"  # Your chat ID

async def send_test_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text="🚀 Melieboombot is online!")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(send_test_message())
