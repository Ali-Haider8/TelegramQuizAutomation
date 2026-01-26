from telegram import Bot
from telegram.error import RetryAfter
import time
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = "@EnglishQuizzesCSUoK"

bot = Bot(token=BOT_TOKEN)

def load_message_from_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

MESSAGE_FILE = "pinned_message_english.md"
message_text = load_message_from_file(MESSAGE_FILE)

while True:
    try:
        bot.send_message(
            chat_id=CHAT_ID,
            text=message_text,
            parse_mode="Markdown",
            disable_web_page_preview=True,
            disable_notification=True
        )
        print("Pinned message sent successfully ✅")
        break

    except RetryAfter as e:
        print(f"Flood control… sleeping {e.retry_after}s")
        time.sleep(e.retry_after + 1)