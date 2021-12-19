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


def demo():
    cwd = os.getcwd()

    fname = input("Please specify the image you want to use for encoding: ")
    message = input("Please specify the message you want to encode: ")


    #prepare_image("resources/original.png", "original.png")
    sender =  Sender( fname, message, cwd)
    wname = fname.replace(".png", "_encoded.png")
    sender.encode_message_in_image(fname=wname)

    print(f"Message encoded into image {wname}")


if __name__ == "__main__":
    demo()





