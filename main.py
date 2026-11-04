import telebot
import os
from PIL import Image, ImageDraw, ImageFont
import io

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👹 ابعتلي أي كلمة و نعملك بيها لوقو ملعون بخلفية سوداء")

@bot.message_handler(func=lambda message: True)
def make_logo(message):
    text = message.text
    
    img = Image.new('RGB', (1080, 1080), color='black')
    draw = ImageDraw.Draw(img)
    
    # فونت كبير مضمون 100%
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 140)
    except:
        font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 140)
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (1080 - text_width) / 2
    y = (1080 - text_height) / 2
    
    # ظل احمر
    draw.text((x+6, y+6), text, fill=(255, 0, 0), font=font)
    # كتابة بيضاء
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    bio = io.BytesIO()
    bio.name = 'logo.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    bot.send_photo(message.chat.id, bio, caption=f"👹 لوقو: {text}")

print("Bot started - Salman Version 🔥")
bot.infinity_polling(skip_pending=True)
    # ظل احمر
    draw.text((x+6, y+6), text, fill=(255, 0, 0), font=font)
    # كتابة بيضاء
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    bio = io.BytesIO()
    bio.name = 'logo.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    bot.send_photo(message.chat.id, bio, caption=f"👹 لوقو: {text}")

print("Bot started - Salman Version 🔥")
bot.infinity_polling(skip_pending=True)
print("Bot started - Salman Version 🔥")
bot.infinity_polling(skip_pending=True)
