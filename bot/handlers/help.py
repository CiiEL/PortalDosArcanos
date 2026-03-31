from telegram import Update
from telegram.ext import ContextTypes

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - iniciar\n/help - ajuda\n/produto - conheça tarólogas e serviços\n/duvidas - perguntas frequentes\n/planos - valores de consulta e pacotes\n/agendar - reservar consulta\n/echo <texto> - repete seu texto\n/hora - hora atual\n/quote - frase de API"
    )
