from PIL import Image
from MessageDecoder import MessageDecoder
from KeyDecoder import KeyDecoder


class Receiver(object):

    def __init__(self, img_name):
        self.__img = Image.open(img_name)
        self.__key_decoder = KeyDecoder("resources/original.jpg")

    def encode_message_in_image(self):
        self.__message_encoder.encode_message(self.__message)
        key = self.__message_encoder.write_img("resources/test.png")  # not sure what this is for
        KeyEncoder(self.__img, key)