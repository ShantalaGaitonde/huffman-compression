import os
import io
import pickle
from bitarray import bitarray
from core import generate_codes


def decode_file(filename):
    arr = bitarray(endian='little')
    with io.open(filename, 'rb') as encoded_file:
        tree_length_length = int(encoded_file.read(1).decode("utf-8"))
        tree_length = int(encoded_file.read(tree_length_length).decode("utf-8"))
        huffman_tree_node = pickle.loads(encoded_file.read(tree_length))
        padded_bits = int(encoded_file.read(1).decode("utf-8"))
        encoded_bytes_length_length = int(encoded_file.read(4).decode("utf-8"))
        encoded_bytes_length = int(encoded_file.read(encoded_bytes_length_length).decode("utf-8"))
        encoded_bytes = encoded_file.read(encoded_bytes_length)
        arr.frombytes(encoded_bytes)
    huffman_code_dict = {}
    generate_codes(huffman_code_dict, huffman_tree_node, "")
    return huffman_decode_internal(filename, arr, huffman_code_dict, padded_bits)


def huffman_decode(filename, huffman_code_dict, padded_bits):
    arr = bitarray(endian='little')
    with open(filename, 'rb') as fh:
        arr.fromfile(fh)
    return huffman_decode_internal(filename, arr, huffman_code_dict, padded_bits)

def huffman_decode_internal(filename, arr, huffman_code_dict, padded_bits):
    length_decoded_file = len(arr) - padded_bits
    new_arr = arr[0:length_decoded_file]
    decoded_list = new_arr.decode(huffman_code_dict)
    decoded_text = ''.join(decoded_list)
    with open(os.path.splitext(filename)[0].split('_')[0] + "_decoded.txt", 'w') as fh:
        fh.write(decoded_text)
    return os.path.splitext(filename)[0].split('_')[0] + "_decoded.txt"
