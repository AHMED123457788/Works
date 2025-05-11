from flask import Flask, request
from telegram import Bot, Update, InputMediaVideo
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

    # الكلمات المدعومة لجميع الفيديوات
    pattern = re.compile(r'\b(moto|funny|brazil|gun|cazy|fight|fights|combat|mma|box|ufc)\b', re.IGNORECASE)
    dp.add_handler(MessageHandler(Filters.text & Filters.regex(pattern), handle_message))

    dp.process_update(update)
    return 'ok'

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    if text in ["fight", "fights", "combat", "mma", "box", "ufc"]:
        send_fight_album(update)
    else:
        send_general_album(update)

def send_general_album(update: Update):
    media_group = [
        InputMediaVideo("https://t.me/archive_360/3"),
        InputMediaVideo("https://t.me/archive_360/4"),
        InputMediaVideo("https://t.me/daily_619/66"),
    ]
    update.message.reply_media_group(media_group)

def send_fight_album(update: Update):
    media_group = [
        InputMediaVideo("https://t.me/fiightsclub/1166"),
        InputMediaVideo("https://t.me/fiightsclub/1168"),
        InputMediaVideo("https://t.me/fiightsclub/1163"),
        InputMediaVideo("https://t.me/fiightsclub/1161"),
        InputMediaVideo("https://t.me/fiightsclub/1159"),
        InputMediaVideo("https://t.me/fiightsclub/1155"),
        InputMediaVideo("https://t.me/fiightsclub/1152"),
        InputMediaVideo("https://t.me/fiightsclub/1150"),
        InputMediaVideo("https://t.me/fiightsclub/1149"),
        InputMediaVideo("https://t.me/fiightsclub/1146"),
    ]
    update.message.reply_media_group(media_group)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
