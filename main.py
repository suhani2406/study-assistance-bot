from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
)

from features.pdf_summary import handle_pdf
from features.pomodoro import pomodoro
from features.reminder import reminder
from features.note import note
from features.mood import mood
from features.summary_utils import get_daily_summary

import logging


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
# BOT_TOKEN = "8188266587:AAHSsYC6yaMRmA4EasIPOPZki-dQ0_xn0ck"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

app = ApplicationBuilder().token(BOT_TOKEN).build()

# ✅ Correct start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Study Bot Commands:\n"
        "/pomodoro - Start a focus session\n"
        "/reminder <task> in <minutes/hours>\n"
        "/note <your note>\n"
        "/mood - Get a study tip based on your mood\n"
        "/summary - Get today’s study summary\n"
        "Send me a PDF 📄 to summarize!"
    )

# Registering all handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("pomodoro", pomodoro))
app.add_handler(CommandHandler("reminder", reminder))
app.add_handler(CommandHandler("note", note))
app.add_handler(CommandHandler("mood", mood))
app.add_handler(CommandHandler("summary", get_daily_summary))
app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))

print("🤖 Bot is running. Waiting for commands or PDFs...")
app.run_polling()
