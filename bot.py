import os
from dotenv import load_dotenv

from database.database import init_database

from handlers.search_handler import search_handler
from handlers.start_handler import start_handler

from telegram import Update
from telegram.ext import (
    Application
)

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


def main():
    init_database()

    app = Application.builder().token(TOKEN).build()

    app.add_handler(start_handler)

    app.add_handler(search_handler)

    print("Bot lancé 🚀")

    app.run_polling()


if __name__ == "__main__":
    main()