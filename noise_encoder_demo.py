import os
import shutil
from classes.Sender import Sender
import string
import random


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
    message = ''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase, k=100000))


    #prepare_image("resources/original.png", "original.png")
    sender =  Sender( fname, message, cwd)
    wname = fname.replace(".png", "_noise_encoded.png")
    sender.encode_message_in_image(fname=wname)

    print(f"Message encoded into image {wname}")


if __name__ == "__main__":
    demo()