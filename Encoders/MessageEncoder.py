from PIL import Image
import numpy as np
from tqdm import tqdm


class MessageEncoder(object):

    def __init__(self, img_name):
        self.__key = []
        self.__key_set = set()
        self.__img = Image.open(img_name)

    @classmethod
    def __pad_msg(cls, msg: bytes):
        pad_len = 3 - len(msg) % 3
        return msg + b'\0' * pad_len

    def __get_index(self, ):
        width, height = self.__img.size
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        if (x, y) in self.__key_set:
            return self.__get_index()
        else:
            self.__key.append((x, y))
            self.__key_set.add((x, y))
            return x, y

    def write_img(self, file_name):
        self.__img.save(file_name, "PNG")
        return self.__key

    def encode_message(self, msg: str):
        raw_msg = self.__pad_msg(msg.encode())
        for i in tqdm(range(0, len(raw_msg), 3), "encoding"):
            index = self.__get_index()
            if self.__img.format == "PNG":
                alpha = self.__img.getpixel(index)[3]
                self.__img.putpixel(index,(raw_msg[i],raw_msg[i+1],raw_msg[i+2], alpha))
            else:
                self.__img.putpixel(index,(raw_msg[i],raw_msg[i+1],raw_msg[i+2], 255))
        return self.__key
