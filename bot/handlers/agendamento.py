from telegram import Update
from telegram.ext import ContextTypes

# fluxos de conversas
TAROLOGA, PLANO, NOME, DATA = range(4)

async def agendar_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = (
        "✨ Vamos agendar sua consulta!\n\n"
        "Escolha a taróloga digitando um número:\n"
        "1 - Maria Arcana (amor e autoestima)\n"
        "2 - Luna Estrela (carreira e finanças)\n"
        "3 - Hélio Solar (espiritualidade e propósito)"
    )
    await update.message.reply_text(texto)
    return TAROLOGA


async def agendar_tarologa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    escolha = update.message.text.strip()
    tarologas = {
        "1": "Maria Arcana",
        "2": "Luna Estrela",
        "3": "Hélio Solar",
    }

    if escolha not in tarologas:
        await update.message.reply_text("Taróloga inválida. Digite 1, 2 ou 3.")
        return TAROLOGA

    context.user_data["tarologa"] = tarologas[escolha]
    await update.message.reply_text(
        "Ótimo! Agora escolha o plano:\n"
        "1 - Consulta individual (R$120)\n"
        "2 - Pacote 3 consultas (R$324)\n"
        "3 - Pacote 5 consultas (R$510)"
    )
    return PLANO


async def agendar_plano(update: Update, context: ContextTypes.DEFAULT_TYPE):
    escolha = update.message.text.strip()
    planos = {
        "1": "Consulta individual - R$120",
        "2": "Pacote 3 consultas - R$324",
        "3": "Pacote 5 consultas - R$510",
    }

    if escolha not in planos:
        await update.message.reply_text("Opção inválida. Digite 1, 2 ou 3.")
        return PLANO

    context.user_data["plano"] = planos[escolha]
    await update.message.reply_text("Perfeito! Agora me diga seu nome completo para reserva.")
    return NOME


async def agendar_nome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.message.text.strip()
    if not nome:
        await update.message.reply_text("Nome inválido. Por favor digite seu nome completo.")
        return NOME

    context.user_data["nome"] = nome
    await update.message.reply_text("Perfeito. Qual data e horário você prefere? (ex: 03/04/2026 19:00)")
    return DATA


from datetime import datetime
from zoneinfo import ZoneInfo

async def agendar_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data_input = update.message.text.strip()

    try:
        data_obj = datetime.strptime(data_input, "%d/%m/%Y %H:%M")
        data_obj = data_obj.replace(tzinfo=ZoneInfo("America/Sao_Paulo"))
    except Exception:
        await update.message.reply_text("Formato inválido. Use dd/mm/yyyy HH:MM, ex: 03/04/2026 19:00")
        return DATA

    now = datetime.now(tz=ZoneInfo("America/Sao_Paulo"))
    if data_obj <= now:
        await update.message.reply_text("Data passada não permitida. Informe data/hora futura (dd/mm/yyyy HH:MM).")
        return DATA

    context.user_data["data"] = data_input

    resumo = (
        f"📌 Agendamento solicitado:\n"
        f"Taróloga: {context.user_data.get('tarologa', 'a definir')}\n"
        f"Plano: {context.user_data.get('plano')}\n"
        f"Nome: {context.user_data.get('nome')}\n"
        f"Data/hora sugerida: {data_input} (dd/mm/yyyy hh:mm)\n\n"
        "✅ Enviaremos uma confirmação em breve e link de pagamento.\n"
        "Obrigado!"
    )

    await update.message.reply_text(resumo)
    return -1


async def agendar_cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Agendamento cancelado. Use /agendar para tentar novamente.")
    return -1
