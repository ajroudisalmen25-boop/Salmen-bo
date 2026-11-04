import telebot
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io
import requests
import random

TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

# فونت عربي قوي
FONT_URL = "https://github.com/rastikerdar/vazirmatn/raw/master/fonts/ttf/Vazirmatn-Black.ttf"
FONT_PATH = "/tmp/vazir_black.ttf"

if not os.path.exists(FONT_PATH):
    r = requests.get(FONT_URL)
    with open(FONT_PATH, 'wb') as f:
        f.write(r.content)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🧠🔥 ابعتلي كلمة نعملك بيها لوقو ميتال فيه عقل ملعون")

@bot.message_handler(func=lambda message: True)
def make_logo(message):
    text = message.text
    
    img = Image.new('RGB', (1080, 1080), color=(5, 0, 10)) # اسود بنفسجي
    draw = ImageDraw.Draw(img)
    
    # فونت ضخم 280
    font = ImageFont.truetype(FONT_PATH, 280)
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (1080 - text_width) / 2
    y = (1080 - text_height) / 2
    
    # 1. ايفيكت "عقل": خطوط عشوائية كي العروق
    for _ in range(80):
        x1 = random.randint(int(x-50), int(x+text_width+50))
        y1 = random.randint(int(y-50), int(y+text_height+50))
        x2 = x1 + random.randint(-40, 40)
