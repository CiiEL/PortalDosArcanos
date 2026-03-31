from telegram import Update
from telegram.ext import ContextTypes

async def produto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "� *PortalDosArcanos - Consultas de Tarot*\n\n"
        "Apresentamos tarólogas especializadas com atendimento personalizado.\n"
        "• Nome da taróloga 1 - Especialidade<br>\n"
        "• Nome da taróloga 2 - Especialidade<br>\n"
        "• Nome da taróloga 3 - Especialidade\n\n"
        "/planos para ver valores de consulta individual e pacotes.\n"
        "Caso tenha uma taróloga específica em mente, responda aqui."
    )
    await update.message.reply_text(texto, parse_mode='Markdown')
