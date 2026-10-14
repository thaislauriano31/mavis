from telegram import Update
from telegram.ext import ContextTypes
from services.roulette_service import RouletteService

roulette_service = RouletteService()

async def roulette_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    
    if len(args) < 2:
        await update.message.reply_text("⚠️ Uso correto: `/roleta <minutos> <energia>`\nExemplo: `/roleta 30 baixa`", parse_mode="Markdown")
        return

    try:
        max_duration = int(args[0])
        energy_level = args[1].lower()
    except ValueError:
        await update.message.reply_text("❌ O tempo deve ser um número inteiro em minutos.")
        return

    resultado = roulette_service.spin(max_duration, energy_level)

    if isinstance(resultado, str):
        await update.message.reply_text(resultado)
    else:
        texto = "🎰 **Tarefas sorteadas na roleta:**\n\n"
        for t in resultado:
            texto += f"• **{t['title']}** ({t['duration_minutes']} min)\n"
        await update.message.reply_text(texto, parse_mode="Markdown")