from telegram import Update
from telegram.ext import ContextTypes
from bot.services.quote_service import fetch_quote
from bot.config import API_QUOTE_URL

async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Buscando frase da API... aguarde")
    try:
        loop = context.application.loop
        resultado = await loop.run_in_executor(None, fetch_quote, API_QUOTE_URL)
        await update.message.reply_text(resultado)
    except Exception:
        await update.message.reply_text("Desculpe, não consegui obter a frase da API. Tente mais tarde.")
