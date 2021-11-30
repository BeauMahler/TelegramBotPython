# install python-telegram-bot package

import logging

from telegram.ext import Updater, MessageHandler, Filters

from telegram import *
from io import BytesIO

bot = Updater("2136505229:AAFQ9WIDMqSJlxZbOfAVssKrIDcwcRKMxh8", use_context=True)  # @AdvNetSecbot

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
#    self.img = Image.open(img_name)
    print("i am here")
    update.message.reply_text('decrypt photo')
    file = bot.getFile(update.message.photo[-1].file_id)
    print("file_id: " + str(update.message.photo[-1].file_id))
   # python3 ./stego.py
    exec(open('./stego.py').read())
# msg = ""
#	for i in tqdm(key, "decoding"):
#	r,g,b = self.img.getpixel(i)
#	msg += chr(r)+chr(g)+chr(b)

#	return msg

    f = BytesIO(file.download_as_bytearray())
    context.bot.send_message(chat_id=update.message.chat_id, text='Joe')


def main():
    # Get the dispatcher to register handlers
    dp = bot.dispatcher

    # on received text or photo message
    dp.add_handler(MessageHandler(Filters.document, decrypt))
    dp.add_handler(MessageHandler(Filters.text, echo))
    # dp.add_handler(MessageHandler(Filters.photo, encode_message))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    bot.start_polling()

    bot.idle()

    bot.stop()


if __name__ == '__main__':
    main()
