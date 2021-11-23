# install python-telegram-bot package

import logging

from telegram.ext \
    import Updater, MessageHandler, Filters


from telegram import *
from io \
    import BytesIO

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
    # update.message.reply_text('decrypt photo')
    file = bot.getFile(update.message.photo[-1].file_id)
    print("file_id: " + str(update.message.photo[-1].file_id))

    # f = BytesIO(file.download_as_bytearray())
    # context.bot.send_message(chat_id=update.message.chat_id, text='Joe')


def main():
    # Get the dispatcher to register handlers
    dp = bot.dispatcher

    # on received text or photo message
    dp.add_handler(MessageHandler(Filters.photo, decrypt))
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    bot.start_polling()

    bot.idle()

    bot.stop()

if __name__ == '__main__':
    main()