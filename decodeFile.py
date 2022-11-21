import os
from bitarray import bitarray
arr = bitarray(endian='little')


def huffman_decode(filename, huffman_code_dict, padded_bits):
    decoded_file = open(os.path.splitext(filename)[0].split('_')[0]+"_decoded.txt", 'w')
    with open(filename, 'rb') as fh:
        arr.fromfile(fh)
    length_decoded_file = len(arr) - padded_bits
    new_arr = arr[0:length_decoded_file]
    decoded_list = new_arr.decode(huffman_code_dict)
    decoded_text = ''.join(decoded_list)
    with open(os.path.splitext(filename)[0].split('_')[0]+"_decoded.txt", 'w') as fh:
        fh.write(decoded_text)
    decoded_file.close()
