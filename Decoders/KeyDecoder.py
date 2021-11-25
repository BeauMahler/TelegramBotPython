import struct

jpg_eof = b'\xff\xd9'
png_eof = b'\x00IEND\xaeB`\x82'
jpg_ex = ".jpg"
png_ex = ".png"


class KeyDecoder(object):

    def __init__(self, img_name):
        self.__img = open(img_name, "rb")

    @classmethod
    def __reconstruct_input(cls, unpacked):
        to_list = list(unpacked)
        reconstructed = []
        for i in range(0, len(to_list), 2):
            reconstructed.append((to_list[i], to_list[i + 1]))
        return reconstructed

    @classmethod
    def __extract_secret(cls, img):
        s = img.read()
        secret = s.split(png_eof)[1]
        print("secret extracted")
        return secret

    def decode_key(self):
        # extraction from image
        extracted = self.__extract_secret(self.__img)
        self.__img.close()
        print("extracted secret: {}".format(extracted))

        # unpacking
        unpacked = struct.unpack('{}h'.format(len(extracted) // 2), extracted)
        print("unpacked secret: {}".format(unpacked))

        # reconstruct original list
        reconstructed = self.__reconstruct_input(unpacked)
        print("reconstructed list: {}".format(reconstructed))

        return reconstructed
