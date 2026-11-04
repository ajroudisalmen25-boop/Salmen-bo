import telebot
import os
from PIL import Image, ImageDraw, ImageFont
import io

# التوكن متاع البوت من الـ Secrets في Fly.io
TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👹 ابعتلي أي كلمة و نعملك بيها لوقو ملعون بخلفية سوداء")

@bot.message_handler(func=lambda message: True)
def make_logo(message):
    text = message.text
    
    # 1. نعملو تصويرة سوداء 1080x1080
    img = Image.new('RGB', (1080, 1080), color='black')
    draw = ImageDraw.Draw(img)
    
    # 2. نجيبو فونت كبير
    try:
        # جرب فونت Arial كان موجود
        font = ImageFont.truetype("arial.ttf", 140)
    except:
        # كان ما لقاش يستعمل الافتراضي
        font = ImageFont.load_default(size=140)
    
    # 3. نحسبو وين نحطو الكتابة في الوسط بالضبط
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (1080 - text_width) / 2
    y = (1080 - text_height) / 2
    
    # 4. نرسمو الظل الاحمر الاول
    draw.text((x+6, y+6), text, fill=(255, 0, 0), font=font)
    # 5. نرسمو الكتابة البيضاء الفوق
    draw.text((x, y), text, fill=(255, 255, 255), font=font)
    
    # 6. نبعتو التصويرة
    bio = io.BytesIO()
    bio.name = 'logo.png'
    img.save(bio, 'PNG')
    bio.seek(0)
    bot.send_photo(message.chat.id, bio, caption=f"👹 لوقو: {text}")

print("Bot started - Salman Version 🔥")
bot.infinity_polling(skip_pending=True)
