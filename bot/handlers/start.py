from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "🔮 *Bem-vinda(o) ao PortalDosArcanos!*\n\n"
        "Aqui você encontra atendimento completo para tarólogas e consultas de Tarot.\n\n"
        "📌 Comandos úteis:\n"
        "- /produto: conhecer o serviço e profissionais\n"
        "- /duvidas: perguntas frequentes\n"
        "- /planos: ver valores de consultas e pacotes\n"
        "- /agendar: reservar consulta\n"
        "- /help: outros comandos\n\n"
        "Vamos construir a melhor página de vendas e agendamento para suas consultas."
    )
    await update.message.reply_text(texto, parse_mode='Markdown')
