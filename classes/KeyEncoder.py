import struct


class KeyEncoder(object):

    def __init__(self, img_name, key):
        self.img = open(img_name, "ab")
        self.key = key

    def encode_key(self):
        to_pack = []

        # pack input list
        for el in self.key:
            to_pack.append(el[0])
            to_pack.append(el[1])
        packed_key = struct.pack('{}h'.format(len(to_pack)), *to_pack)
        print("packed_key to inject: {}".format(packed_key))

        # inject packed_key at the end of the file
        self.img.write(packed_key)
        print("packed_key injected")
        self.img.close()
