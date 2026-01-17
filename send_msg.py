from telegram import Bot
from telegram.error import RetryAfter
import time



bot = Bot(token=TOKEN)
bot = Bot(token=TOKEN)

message_text = (
    "📢 *تنبيه هام لضمان النجاح والتفوق*\n\n"
    "🔹 *المفتاح الحقيقي للنجاح:*\n"
    "• الدراسة العملية والمركزة للمصادر الأساسية أولاً.\n"
    "• المراجعة الجادة هي الضمان الوحيد للتفوق.\n\n"
    "🔹 *الهدف من هذه الاختبارات:*\n"
    "• وسيلة إضافية للتسلية والفائدة فقط.\n"
    "• تنشيط الذاكرة والتعرف على نمط الأسئلة.\n"
    "• اختبار دقة دراستك بأسلوب تفاعلي بعد المذاكرة."
)

while True:
    try:
        bot.send_message(
            chat_id=CHAT_ID,
            text=message_text,
            disable_web_page_preview=True,
            disable_notification=True,
            parse_mode='Markdown'  # أضف هذا السطر هنا
        )
        print("Message sent successfully ✅")
        break

    except RetryAfter as e:
        time.sleep(e.retry_after + 1)