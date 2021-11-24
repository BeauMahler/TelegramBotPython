import os
import io
import PIL.Image as Image


def read_image(path):
    with open(path, "rb") as f:
        return bytearray(f.read())


def main():
    cwd = os.getcwd()

    input_list = [(1, 2), (3, 4), (12, 4)]

    byte_list = []

    # convert input_list
    for el in input_list:
        temp = str(el[0]).encode() + str(el[1]).encode()
        byte_list.insert(len(byte_list), temp)

    secret = b''.join(byte_list)

    print(secret)

    # bytes_image = read_image(cwd + '\\resources\\original.jpg')
    # print(bytes_image[-20:])

    f = open(cwd + '\\original.jpg', 'a')

    f.write('\\d9\\d2\\d9')

    f.close()

    # bytes_image.extend(secret)

    bytes_image2 = read_image(cwd + '\\original.jpg')

    # print(bytes_image2[-20:])

    # image = Image.open(io.BytesIO(bytes_image2))

    # image.save("original.jpg")


if __name__ == '__main__':
    main()
