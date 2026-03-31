from telegram import Update
from telegram.ext import ContextTypes

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Desculpe, não entendi. Use /help.")
