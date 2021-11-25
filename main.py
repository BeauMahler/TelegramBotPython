import os
import struct
import shutil

jpg_eof = b'\xff\xd9'
png_eof = b'\x00IEND\xaeB`\x82'
jpg_ex = ".jpg"
png_ex = ".png"


def extract_secret(path):
    with open(path, "rb") as f:
        s = f.read()
        secret = s.split(png_eof)[1]
        print("secret extracted")
        return secret


def prepare_image(sourcefile, directory):
    res = shutil.copy2(sourcefile, directory + "\\original" + png_ex)
    print("copied image from {} to {}".format(sourcefile, res))


def reset_image(file):
    if os.path.exists(file):
        os.remove(file)
        print("removed file " + file)
    else:
        print("The file does not exist")


def reconstruct_input(unpacked):
    to_list = list(unpacked)
    reconstructed = []
    for i in range(0, len(to_list), 2):
        reconstructed.append((to_list[i], to_list[i + 1]))
    return reconstructed


def main():
    cwd = os.getcwd()
    input_list = [(1, 2), (3, 4), (4000, 4)]  # this will be given later
    to_pack = []

    # pack input list
    for el in input_list:
        to_pack.append(el[0])
        to_pack.append(el[1])

    secret = struct.pack('{}h'.format(len(to_pack)), *to_pack)
    print("secret to inject: {}".format(secret))

    # preparation for injection
    prepare_image(cwd + '\\resources\\original' + png_ex, cwd)

    # write secret at the end of the file
    f = open(cwd + '\\original' + png_ex, 'ab')
    f.write(secret)
    print("secret injected")
    f.close()

    # extraction from image
    extracted = extract_secret(cwd + '\\original' + png_ex)
    print(len(extracted))
    print(len(to_pack))
    unpacked = struct.unpack('{}h'.format(len(extracted)//2), extracted)
    print("extracted secret: {}".format(extracted))
    print("unpacked secret: {}".format(unpacked))

    # reconstruct original list
    print("reconstructed list: {}".format(reconstruct_input(unpacked)))

    # cleanup for next run
    reset_image(cwd + '\\original' + png_ex)


if __name__ == '__main__':
    main()
