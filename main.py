from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackContext
import os
import re

TOKEN = os.environ.get("BOT_TOKEN")
bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is running!'

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dp = Dispatcher(bot, None, workers=0)

    # الكلمات المدعومة
    pattern = re.compile(r'\b(moto|funny|brazil|gun|cazy)\b', re.IGNORECASE)
    dp.add_handler(MessageHandler(Filters.text & Filters.regex(pattern), send_video))
    
    dp.process_update(update)
    return 'ok'

def send_video(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    videos = [
        "https://t.me/archive_360/3",
        "https://t.me/archive_360/4",
        "https://t.me/daily_619/66"
    ]
    # إرسال كل فيديو واحدًا تلو الآخر
    for video in videos:
        bot.send_video(chat_id=chat_id, video=video)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
