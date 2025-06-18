from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters
from config.settings import TELEGRAM_BOT_TOKEN
from bot.handlers import handle_message, start

def run_bot():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))  # اضافه شد
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("ROBOT IS RUNNING...")
    
    app.run_polling()
