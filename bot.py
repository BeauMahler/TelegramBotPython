# install python-telegram-bot package
import os
import logging

from classes.Receiver import Receiver
from telegram.ext import Updater, MessageHandler, Filters

from telegram import *
from io import BytesIO

bot = Updater("2103014393:AAGzPHpqhGhksJpP02w6X5omhrUhhzcw4L4", use_context=True)  # @AdvNetSecbot

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def echo(update, context):
    update.message.reply_text('message received: ' + update.message.text)


# error handling
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


# CODE FOR DECRYPTING PHOTO MESSAGE
def decrypt(update, context):
    message = "this is the secret message"

    receiver = Receiver(os.getcwd() + '\\' + context.bot.get_file(update.message.document).download())
    received = receiver.retrieve_message()

    assert True, message == received


def main():
    # Get the dispatcher to register handlers
    dp = bot.dispatcher

    # on received text or photo message
    dp.add_handler(MessageHandler(Filters.document, decrypt))
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    bot.start_polling()

    bot.idle()

    bot.stop()


if __name__ == '__main__':
    main()
