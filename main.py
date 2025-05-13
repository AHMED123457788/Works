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

    pattern = re.compile(r'\b(moto|funny|brazil|gun|cazy|fight|fights|combat|mma|box|ufc|car|accident|vehicle|voiture|road|ride|run|police|security|guard|force|forces|animal|wild|animals|toros|toro|spain|bull|mexic|mexico|smile|joke|fun|wars|war)\b', re.IGNORECASE)
    dp.add_handler(MessageHandler(Filters.text & Filters.regex(pattern), handle_message))

    dp.process_update(update)
    return 'ok'

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    if text in ["fight", "fights", "combat", "mma", "box", "ufc"]:
        send_album_A(update)
    elif text in ["car", "accident", "vehicle", "voiture", "road", "ride", "run"]:
        send_album_B(update)
    elif text in ["moto", "funny", "brazil", "gun", "cazy"]:
        send_album_C(update)
    elif text in ["war", "wars"]:
        send_album_D(update)
    elif text in ["fun", "funny", "smile", "joke"]:
        send_album_E(update)
    elif text in ["animal", "wild", "animals"]:
        send_album_F(update)
    elif text in ["police", "security", "guard", "force", "forces"]:
        send_album_G(update)

def send_album_A(update: Update):  # قائمة A: القتال
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

def send_album_B(update: Update):  # قائمة B: حوادث السيارات
    media_group = [
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1384"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1469"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1435"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1416"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1410"),
    ]
    update.message.reply_media_group(media_group)

def send_album_C(update: Update):  # قائمة C: moto والكلمات القديمة
    media_group = [
        InputMediaVideo("https://t.me/archive_360/3"),
        InputMediaVideo("https://t.me/archive_360/4"),
        InputMediaVideo("https://t.me/daily_619/66"),
    ]
    update.message.reply_media_group(media_group)

def send_album_D(update: Update):  # قائمة D: الحرب
    media_group = [
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1433"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1426"),
    ]
    update.message.reply_media_group(media_group)

def send_album_E(update: Update):  # قائمة E: المضحك
    media_group = [
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1427"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1421"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1420"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1410"),
    ]
    update.message.reply_media_group(media_group)

def send_album_F(update: Update):  # قائمة F: الحيوانات
    media_group = [
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1418"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1421"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1408"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1383"),
    ]
    update.message.reply_media_group(media_group)

def send_album_G(update: Update):  # قائمة G: الشرطة
    media_group = [
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1414"),
        InputMediaVideo("https://t.me/kaotic_com_seegore_bestgore/1390"),
    ]
    update.message.reply_media_group(media_group)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
