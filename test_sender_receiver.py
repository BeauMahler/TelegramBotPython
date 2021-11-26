import os
import shutil
from classes.Sender import Sender
from classes.Receiver import Receiver

jpg_ex = ".jpg"
png_ex = ".png"


def prepare_image(sourcefile, directory):
    res = shutil.copy2(sourcefile, directory + "\\original" + png_ex)
    print("copied image from {} to {}".format(sourcefile, res))


def reset_image(file):
    if os.path.exists(file):
        os.remove(file)
        print("removed file " + file)
    else:
        print("The file does not exist")


def test():
    cwd = os.getcwd()

    message = "this is the secret message"

    # preparation for injection
    prepare_image(cwd + '\\resources\\original' + png_ex, cwd)

    sender = Sender(cwd + "\\original" + png_ex, message, cwd)
    sender.encode_message_in_image()

    receiver = Receiver(cwd + "\\encoded" + png_ex)
    received = receiver.retrieve_message()

    # clean up
    reset_image(cwd + "\\encoded" + png_ex)
    reset_image(cwd + "\\original" + png_ex)

    assert True, message == received
