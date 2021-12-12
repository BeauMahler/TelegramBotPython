import os
import shutil
from classes.Sender import Sender
from classes.Receiver import Receiver

jpg_ex = ".jpg"
png_ex = ".png"


def prepare_image(sourcefile, dest):
    res = shutil.copy2(sourcefile, dest)
    print("copied image from {} to {}".format(sourcefile, res))


def reset_image(file):
    if os.path.exists(file):
        os.remove(file)
        print("removed file " + file)
    else:
        print("The file does not exist")


def test():
    cwd = os.getcwd()
    message = "this is a secret message"

    prepare_image("resources/original.png", "original.png")
    sender =  Sender( "original.png", message, cwd)
    sender.encode_message_in_image()

    receiver = Receiver("encoded.png")
    received = receiver.retrieve_message()

    reset_image("original.png")
    reset_image("encoded.png")

    assert True, message == received

test()
print("Test Passed")