from Encoders.MessageEncoder import MessageEncoder
from Decoders.MessageDecoder import MessageDecoder


def test():
    message = "does it work again today"

    a = MessageEncoder("resources/original.png")
    key = a.encode_message(message)

    a.write_img("resources/encoded.png")  # not sure what this is for

    b = MessageDecoder("resources/encoded.png")

    decoded = b.decode_msg(key)

    trimmed = decoded.rstrip("\x00")

    assert True, message == trimmed
