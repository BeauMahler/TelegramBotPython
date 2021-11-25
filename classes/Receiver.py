from Decoders.MessageDecoder import MessageDecoder
from Decoders.KeyDecoder import KeyDecoder


class Receiver(object):

    def __init__(self, img_name):
        self.__key_decoder = KeyDecoder(img_name)
        self.__img_name = img_name

    def retrieve_message(self):
        key = self.__key_decoder.decode_key()
        message_decoder = MessageDecoder(self.__img_name)
        message = message_decoder.decode_msg(key)
        return message
