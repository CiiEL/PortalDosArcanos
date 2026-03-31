import logging
from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters
from bot.config import TOKEN
from bot.handlers.start import start
from bot.handlers.help import help_command
from bot.handlers.echo import echo
from bot.handlers.hora import hora
from bot.handlers.quote import quote
from bot.handlers.produto import produto
from bot.handlers.duvidas import duvidas
from bot.handlers.planos import planos
from bot.handlers.agendamento import agendar_start, agendar_tarologa, agendar_plano, agendar_nome, agendar_data, agendar_cancel, TAROLOGA, PLANO, NOME, DATA
from bot.handlers.unknown import unknown

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("produto", produto))
    app.add_handler(CommandHandler("duvidas", duvidas))
    app.add_handler(CommandHandler("planos", planos))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("hora", hora))
    app.add_handler(CommandHandler("quote", quote))

    agendamento_conv = ConversationHandler(
        entry_points=[CommandHandler("agendar", agendar_start)],
        states={
            TAROLOGA: [MessageHandler(filters.TEXT & ~filters.COMMAND, agendar_tarologa)],
            PLANO: [MessageHandler(filters.TEXT & ~filters.COMMAND, agendar_plano)],
            NOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, agendar_nome)],
            DATA: [MessageHandler(filters.TEXT & ~filters.COMMAND, agendar_data)],
        },
        fallbacks=[CommandHandler("cancel", agendar_cancel)],
        allow_reentry=True,
    )

    app.add_handler(agendamento_conv)
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    logger.info("Bot Marcela iniciado")
    app.run_polling()


if __name__ == "__main__":
    main()
