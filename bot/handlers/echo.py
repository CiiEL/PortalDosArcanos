from telegram import Update
from telegram.ext import ContextTypes

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)
    if not text:
        await update.message.reply_text("Use: /echo texto")
        return
    await update.message.reply_text(text)
