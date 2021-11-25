import os
import shutil
from classes.KeyEncoder import KeyEncoder
from classes.KeyDecoder import KeyDecoder

jpg_eof = b'\xff\xd9'
png_eof = b'\x00IEND\xaeB`\x82'
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
    input_list = [(1, 2), (3, 4), (4000, 4)]  # this will be given later

    # preparation for injection
    prepare_image(cwd + '\\resources\\original' + png_ex, cwd)

    # encoder creation
    encoder = KeyEncoder(cwd + '\\original' + png_ex, input_list)

    # encoding
    encoder.encode_key()

    decoder = KeyDecoder(cwd + '\\original' + png_ex)

    res = decoder.decode_key()

    assert True, input_list == res

    # cleanup for next run
    reset_image(cwd + '\\original' + png_ex)
