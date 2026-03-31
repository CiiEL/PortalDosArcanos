from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

async def hora(update: Update, context: ContextTypes.DEFAULT_TYPE):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    await update.message.reply_text(f"Agora são: {agora}")
