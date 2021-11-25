from PIL import Image
from Encoders.MessageEncoder import MessageEncoder
from Encoders.KeyEncoder import KeyEncoder


class Sender(object):

    def __init__(self, img_name, message, save_dir):
        self.__img = Image.open(img_name)
        self.__img_name = img_name
        self.__message = message
        self.__message_encoder = MessageEncoder(img_name)
        self.__save_dir = save_dir

    def encode_message_in_image(self):
        self.__message_encoder.encode_message(self.__message)
        key = self.__message_encoder.write_img(self.__save_dir + "\\encoded.png")
        key_encoder = KeyEncoder("encoded.png", key)
        key_encoder.encode_key()
        self.__img.close()
