import telebot
import os
from PIL import Image, ImageDraw, ImageFont
import io

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👹 ابعتلي أي كلمة تو نعملك بيها لوقو ملعون")

@bot.message_handler(func=lambda message: True)
def make_logo(message):
    text = message.text
    img = Image.new('RGB', (1080, 1080), color='black')
    d = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("arial.ttf", 120)
    except:
        font = ImageFont.load_default()
    
    # نحسبو الوسط
    bbox = d.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    x = (1080 - w) / 2
    y = (1080 - h) / 2
    
    # ظل احمر
    d.text((x+5, y+5), text, fill="red", font=font)
    # كتابة بيضاء الفوق
    d.text((x, y), text, fill="white", font=font)
    
    bio = io.BytesIO()
    bio.name = 'logo.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    bot.send_photo(message.chat.id, bio)

print("Bot started")
bot.infinity_polling()
