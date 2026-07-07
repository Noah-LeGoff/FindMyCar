from database.database import add_user

from telegram import Update
from telegram.ext import (
    CommandHandler,
    ContextTypes
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    add_user(
        user.id,
        user.username,
        user.first_name
    )
    
    await update.message.reply_text(
        "🚗 Bienvenue sur FindMyCar !\n\n"
        "Je t'aiderai à trouver les bonnes affaires automobiles.\n"
        "Utilise /search pour lancer une recherche."
    )

start_handler = CommandHandler("start", start)