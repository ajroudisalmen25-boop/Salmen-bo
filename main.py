import os
import requests
import json
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

BOT_TOKEN = 8928666107:AAFdWctjlr-foi-iuLJnsw0HI0n40jH1qDg
HF_TOKEN = 
ADMIN_ID = 14380228  # ⚠️ مهم: بدل 14380228 حط الـ ID متاعك من @userinfobot
HF_MODEL = "Qwen/Qwen2.5-72B-Instruct"

def load_data():
    try:
        with open('users.json', 'r') as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open('users.json', 'w') as f:
        json.dump(data, f)

users = load_data()
FREE_CREDIT = 20

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    if user_id not in users:
        users[user_id] = {"credit": FREE_CREDIT, "total_used": 0}
        save_data(users)
    await update.message.reply_text(
        f"أهلا بيك في سلمين 🤖\n\n"
        f"🔋 رصيدك الحالي: {users[user_id]['credit']} رسالة\n"
        f"💡 كل رسالة تستهلك 1 من الرصيد\n\n"
        f"لما توفى البطارية، اشحن بـ /charge"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    text = update.message.text
    
    if update.effective_user.id != ADMIN_ID:
        if user_id not in users:
            users[user_id] = {"credit": FREE_CREDIT, "total_used": 0}
        
        if users[user_id]['credit'] <= 0:
            keyboard = [[InlineKeyboardButton("🔋 اشحن البطارية", callback_data="charge")]]
            await update.message.reply_text(
                "⚠️ تم انخفاض الشحن! البطارية فارغة 🔋\n\n"
                "ارجاء انتظر حتى يتم الشحن باش تكمل تحكي معاي",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )
            return
        
        users[user_id]['credit'] -= 1
        users[user_id]['total_used'] += 1
        save_data(users)
    
    if any(word in text for word in ["تصويرة", "صورة", "ارسم"]):
        await update.message.reply_text("ثانية نرسملك... 🎨")
        credit = users.get(user_id, {}).get('credit', '∞')
        await update.message.reply_text(f"هاذي تصويرة: https://picsum.photos/512\n\n🔋 رصيدك: {credit}")
        return
    
    if any(word in text for word in ["رابط", "لينك"]):
        credit = users.get(user_id, {}).get('credit', '∞')
        await update.message.reply_text(f"تفضل:\n🔗 https://google.com\n\n🔋 رصيدك: {credit}")
        return
    
    await context.bot.send
