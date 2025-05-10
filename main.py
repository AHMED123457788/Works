from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackContext
import os

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
    dp.add_handler(MessageHandler(Filters.text & Filters.regex("moto"), send_video))
    dp.process_update(update)
    return 'ok'

def send_video(update: Update, context: CallbackContext):
    update.message.reply_video("https://t.me/a_moment_before/8014", caption="مرحباً! هذا هو الفيديو الخاص بك.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
