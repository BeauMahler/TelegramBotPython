from PIL import Image, ImageFilter
import numpy as np
from tqdm import tqdm

class Encoder(object):


    def __init__(self, img_name):
        self.key = set()
        self.img = Image.open(img_name)


    def encode_message(self,msg:str):
        raw_msg = self._pad_msg(msg.encode())
        for i in tqdm(range(0,len(raw_msg),3), "encoding"):
            index = self._get_index()
            self.img.putpixel(index,(raw_msg[i],raw_msg[i+1],raw_msg[i+2]))
        return list(self.key)

    def write_img(self,file_name):
        self.img.save(file_name, "PNG")
        return self.key

    def _pad_msg(self,msg:bytes):
        pad_len = 3 - len(msg) % 3
        return msg+b'\0'*pad_len

    def _get_index(self,):
        width, height = self.img.size
        x = np.random.randint(0,width)
        y = np.random.randint(0,height)
        if (x,y) in self.key:
            return self._get_index()
        else:
            self.key.add((x,y))
            return (x,y)


class Decoder(object):

    def __init__(self, img_name):
        self.img = Image.open(img_name)


    def decode_msg(self,key):
        msg = ""
        for i in tqdm(key, "decoding"):
            r,g,b = self.img.getpixel(i)
            msg += chr(r)+chr(g)+chr(b)

        return msg


def example():
    a = Encoder("resources/original.jpg")
    a.encode_message("Q"*1000000)

    key = a.write_img("resources/test.png")

    b = Decoder("resources/test.png")
    print(b.decode_msg(key))

example()


