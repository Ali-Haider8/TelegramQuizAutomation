from telegram import Bot
from telegram.error import RetryAfter
import time

TOKEN = "8255957753:AAFnaI7St8vi1DsE5m3Y3POxYsL7GBa3z20"
CHAT_ID = "@MCQCompStructureUOK"   # القناة التي سيتم الإرسال إليها

bot = Bot(token=TOKEN)

message_text = (
    "📌 Computer Structure MCQs\n\n"
    "Join the quiz channel from the link below:\n"
    "انضم إلى قناة الاختبارات المحدثة من الرابط التالي:\n\n"
    "🔗 https://t.me/MCQCompStructureUOK2"
)

while True:
    try:
        bot.send_message(
            chat_id=CHAT_ID,
            text=message_text,
            disable_web_page_preview=False,
            disable_notification=True   # 🔕 إرسال صامت

        )
        print("Message sent successfully ✅")
        break

    except RetryAfter as e:
        wait_time = e.retry_after + 1
        print(f"Flood control, waiting {wait_time} seconds...")
        time.sleep(wait_time)
