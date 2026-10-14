from telegram import Update
from telegram.ext import ContextTypes
from services.parser_service import TaskParserService
from database.repositories.task_repository import TaskRepository

parser_service = TaskParserService()
task_repo = TaskRepository()

async def add_task_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    
    # Ignora se for comando (ex: /start, /roleta)
    if user_text.startswith('/'):
        return

    await update.message.reply_text("🤖 Processando tarefa...")
    
    # 1. Parsing com LLM
    parsed = parser_service.parse_text_to_task(user_text)
    
    # 2. Salva no Supabase
    created = task_repo.create_task(
        title=parsed["title"],
        duration_minutes=parsed["duration_minutes"],
        energy=parsed["energy"],
        priority=parsed["priority"],
        category=parsed["category"]
    )

    mensagem_sucesso = (
        f"✅ **Tarefa Registrada!**\n\n"
        f"📌 **Título:** {created['title']}\n"
        f"⏱️ **Duração:** {created['duration_minutes']} min\n"
        f"⚡ **Energia:** {created['energy']}\n"
        f"🎯 **Prioridade:** {created['priority']}"
    )
    await update.message.reply_text(mensagem_sucesso, parse_mode="Markdown")