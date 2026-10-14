from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from config.settings import TELEGRAM_BOT_TOKEN
from bot.handlers.task_handler import add_task_handler
from bot.handlers.roulette_handler import roulette_handler
from bot.handlers.list_handler import list_tasks_handler, complete_task_callback

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Registar comandos
    app.add_handler(CommandHandler("roleta", roulette_handler))
    app.add_handler(CommandHandler("tarefas", list_tasks_handler))
   
    # Registar clique nos botões inline
    app.add_handler(CallbackQueryHandler(complete_task_callback, pattern="^done_"))

    # Registar mensagens de texto livres (cadastro de tarefas)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_task_handler))

    print("🤖 Mavis está rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()