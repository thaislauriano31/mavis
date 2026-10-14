from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.repositories.task_repository import TaskRepository

task_repo = TaskRepository()

async def list_tasks_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Busca tarefas pendentes
    tasks = task_repo.get_eligible_tasks(max_duration=999, energy_level="baixa") # Ajusta a query no repo se necessário
    
    if not tasks:
        await update.message.reply_text("🎉 Nenhuma tarefa pendente!")
        return

    texto = "📋 **Suas Tarefas Pendentes:**\n\n"
    keyboard = []
    
    for t in tasks:
        texto += f"• {t['title']} ({t['duration_minutes']} min - {t['energy']})\n"
        keyboard.append([InlineKeyboardButton(f"✅ Concluir: {t['title'][:20]}", callback_data=f"done_{t['id']}")])

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(texto, reply_markup=reply_markup, parse_mode="Markdown")

async def complete_task_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    task_id = query.data.replace("done_", "")
    task_repo.mark_as_completed(task_id)
    
    await query.edit_message_text(text="✅ Tarefa concluída com sucesso!")