from PIL import Image
from tqdm import tqdm


class MessageDecoder(object):

    def __init__(self, img_name):
        self.__img = Image.open(img_name)

    def decode_msg(self,key):
        msg = ""
        if len(self.img.getpixel(key[0])) == 4:
            for i in tqdm(key, "decoding"):
                print(self.img.getpixel(i))
                r,g,b, _ = self.img.getpixel(i)
                msg += chr(r)+chr(g)+chr(b)
            return msg
        else:
            for i in tqdm(key, "decoding"):
                print(self.img.getpixel(i))
                r,g,b = self.img.getpixel(i)
                msg += chr(r)+chr(g)+chr(b)
            return msg
