from telegram import Update
from telegram.ext import (
    ConversationHandler,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

BRAND, MODEL, PRICE, KM = range(4)

async def search_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚗 Quelle marque recherches-tu ?"
    )

    return BRAND

async def brand(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["brand"] = update.message.text

    await update.message.reply_text(
        "Quel modèle ?"
    )

    return MODEL

async def model(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["model"] = update.message.text

    await update.message.reply_text(
        "Quel est ton budget maximum (€) ?"
    )

    return PRICE

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["price"] = int(update.message.text)

    await update.message.reply_text(
        "Quel est le kilométrage maximum ?"
    )

    return KM

async def km(update: Update, context: ContextTypes.DEFAULT_TYPE):

    context.user_data["km"] = int(update.message.text)

    from database.database import get_user_by_telegram_id
    from services.search_service import create_search

    telegram_user = update.effective_user

    user = get_user_by_telegram_id(
        telegram_user.id
    )

    create_search(
        user["id"],
        context.user_data["brand"],
        context.user_data["model"],
        context.user_data["price"],
        context.user_data["km"]
    )

    await update.message.reply_text(
        "✅ Recherche enregistrée avec succès !"
    )

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Recherche annulée."
    )

    return ConversationHandler.END

search_handler = ConversationHandler(
    entry_points=[
        CommandHandler("search", search_start)
    ],

    states={

        BRAND: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, brand)
        ],

        MODEL: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, model)
        ],

        PRICE: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, price)
        ],

        KM: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, km)
        ]

    },

    fallbacks=[
        CommandHandler("cancel", cancel)
    ]
)