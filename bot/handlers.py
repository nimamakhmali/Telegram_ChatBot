from telegram import Update
from telegram.ext import ContextTypes
from services.openai_api import ask_openai

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Ask Your Question!!!")
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.chat.send_action(action="typing")
    reply = ask_openai(user_message)
    await update.message.reply_text(reply)   