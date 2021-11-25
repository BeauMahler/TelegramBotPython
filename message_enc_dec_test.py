from classes.MessageEncoder import MessageEncoder
from classes.MessageDecoder import MessageDecoder


def test():
    message = "does it work again today"

    a = MessageEncoder("resources/original.jpg")
    a.encode_message(message)

    key = a.write_img("resources/test.png")  # not sure what this is for
    print(key)

    b = MessageDecoder("resources/test.png")
    decoded = b.decode_msg(key)

    trimmed = decoded.rstrip("\x00")

    assert True, message == trimmed
