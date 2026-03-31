from telegram import Update
from telegram.ext import ContextTypes

async def duvidas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "❓ *Perguntas frequentes - PortalDosArcanos*\n\n"
        "1) Quais serviços vocês oferecem?\n"
        "   - Atendimento de tarot individual, pacotes de consultas, acompanhamento espiritual e leitura personalizada.\n\n"
        "2) Como escolher a taróloga ideal?\n"
        "   - Cada taróloga tem especialidade: amor, carreira e espiritualidade. Use /produto para ver perfis e /agendar para escolher.\n\n"
        "3) Quanto tempo dura cada consulta?\n"
        "   - Consulta individual tem 45 minutos, pacote é agendado conforme preferência com sessões de 50 min.\n\n"
        "4) Posso trocar a taróloga depois de comprar o pacote?\n"
        "   - Sim, estamos flexíveis; a troca pode ser feita antes da próxima sessão, dependendo de disponibilidade.\n\n"
        "5) Como funciona o pacote de consultas?\n"
        "   - Paga-se uma vez, recebe prioridade de agenda e atendimento com a mesma ou qualquer taróloga parceira.\n\n"
        "Dúvida específica? Responda aqui e a equipe retorna em até 2h (horário comercial)."
    )
    await update.message.reply_text(texto, parse_mode='Markdown')
