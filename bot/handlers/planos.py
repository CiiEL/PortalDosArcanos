from telegram import Update
from telegram.ext import ContextTypes

async def planos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "💳 *Planos do PortalDosArcanos*\n\n"
        "*Consulta individual*:\n"
        "• 1 sessão de 45min\n"
        "• Feedback completo\n"
        "R$ 120\n\n"
        "*Pacote 3 consultas*:\n"
        "• Economize 10%\n"
        "• Agendamento preferencial\n"
        "R$ 324 (R$ 108/cada)\n\n"
        "*Pacote 5 consultas*:\n"
        "• Economize 15%\n"
        "• Prioridade de agenda\n"
        "R$ 510 (R$ 102/cada)\n\n"
        "Para reservar, use /agendar e siga o passo a passo."
    )
    await update.message.reply_text(texto, parse_mode='Markdown')
