import os
from bitarray import bitarray
arr = bitarray(endian='little')


def huffman_encode(filename, huffman_code_dict):
    file = open(filename, 'r')
    while 1:
        # read by character
        char = file.read(1)
        if not char:
            break
        arr.encode(huffman_code_dict, char)

    with open(os.path.splitext(filename)[0]+"_encoded.txt", 'wb') as fh:
        arr.tofile(fh)

    return os.path.splitext(filename)[0]+"_encoded.txt", arr.padbits
    file.close()
    encoded_file.close()


