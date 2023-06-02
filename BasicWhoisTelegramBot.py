import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import whois
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the WHOIS Bot! Send me a website URL to retrieve WHOIS data.")


def get_whois_dates(update: Update, context):
    url = update.message.text
    try:
        w = whois.whois(url)

        def send_date_message(date_type, date):
            if isinstance(date, list):
                date = ", ".join([d.strftime("%Y-%m-%d") for d in date])
            elif date:
                date = date.strftime("%Y-%m-%d")
            if date:
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"{date_type}: {date}")

        send_date_message("Creation Date", w.creation_date)
        send_date_message("Updated Date", w.updated_date)
        send_date_message("Expiration Date", w.expiration_date)
    except Exception as e:
        error_message = "Error retrieving WHOIS data. Please try again."
        context.bot.send_message(chat_id=update.effective_chat.id, text=error_message)
        logger.exception(error_message)


def main():
    updater = Updater("REPLACEWITHBOTTOKEN", use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, get_whois_dates))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()