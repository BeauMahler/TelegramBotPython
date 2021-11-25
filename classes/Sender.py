from PIL import Image
from MessageEncoder import MessageEncoder
from KeyEncoder import KeyEncoder


class Sender(object):

    def __init__(self, img_name, message):
        self.__img = Image.open(img_name)
        self.__img_name = img_name
        self.__message = message
        self.__message_encoder = MessageEncoder(img_name)

    def encode_message_in_image(self):
        self.__message_encoder.encode_message(self.__message)
        key = self.__message_encoder.write_img("resources/encoded.png")
        KeyEncoder(self.__img, key)
