from PIL import Image
from tqdm import tqdm


class MessageDecoder(object):

    def __init__(self, img_name):
        self.__img = Image.open(img_name)

    def decode_msg(self, key):
        msg = ""
        if len(self.__img.getpixel(key[0])) == 4:
            for i in tqdm(key, "decoding"):
                r, g, b, _ = self.__img.getpixel(i)
                msg += chr(r) + chr(g) + chr(b)
            return msg
        else:
            for i in tqdm(key, "decoding"):
                r, g, b = self.__img.getpixel(i)
                msg += chr(r) + chr(g) + chr(b)
            return msg
