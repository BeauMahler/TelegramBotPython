from PIL import Image
from tqdm import tqdm


class MessageDecoder(object):

    def __init__(self, img_name):
        self.img = Image.open(img_name)

    def decode_msg(self, key):
        msg = ""
        for i in tqdm(key, "decoding"):
            r, g, b = self.img.getpixel(i)
            msg += chr(r) + chr(g) + chr(b)
        return msg
