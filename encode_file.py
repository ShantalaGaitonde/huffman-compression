import os
import pickle
from bitarray import bitarray
from core import generate_codes, generate_frequency_dictionary, generate_huffmantree

def encode_file(filename):
    text_file = open(filename, "r")
    text = text_file.read()
    text_file.close()
    letter_freq = generate_frequency_dictionary(text)
    root = generate_huffmantree(letter_freq)

    str1 = ""
    print("The huffman tree nodes are \n")
    print_nodes(root)
    huffman_code_dict = {}
    generate_codes(huffman_code_dict, root, str1)
    print("The huffman code dictionary is\n")
    print(huffman_code_dict)
    arr = huffman_encode_to_bitarray(filename, huffman_code_dict)

    pickled_huffman_tree = pickle.dumps(root)
    tree_length = str(len(pickled_huffman_tree))
    tree_length_length = str(len(tree_length))
    print(tree_length_length, tree_length)
    tree_length_bytes = bytes(tree_length_length + tree_length, "utf-8")
    encoded_bytes = arr.tobytes()
    encoded_bytes_length = str(len(encoded_bytes))
    encoded_bytes_length_length = str(len(encoded_bytes_length))
    encoded_bytes_length_bytes = bytes(encoded_bytes_length_length.zfill(4) + encoded_bytes_length, "utf-8")
    with open(os.path.splitext(filename)[0] + "_encoded.txt", 'wb') as fh:
        fh.write(tree_length_bytes)
        fh.write(pickled_huffman_tree)
        fh.write(str(arr.padbits).encode("utf-8"))
        fh.write(encoded_bytes_length_bytes)
        fh.write(encoded_bytes)

    return os.path.splitext(filename)[0] + "_encoded.txt"


def huffman_encode(filename, huffman_code_dict):
    arr = huffman_encode_to_bitarray(filename, huffman_code_dict)
    with open(os.path.splitext(filename)[0]+"_encoded.txt", 'wb') as fh:
        arr.tofile(fh)
    return os.path.splitext(filename)[0]+"_encoded.txt", arr.padbits


def huffman_encode_to_bitarray(filename, huffman_code_dict):
    arr = bitarray(endian='little')
    file = open(filename, 'r')
    while 1:
        # read by character
        char = file.read(1)
        if not char:
            break
        arr.encode(huffman_code_dict, char)
    file.close()
    return arr

def print_nodes(root):
    if root.left is not None:
        print_nodes(root.left)
    if root.right is not None:
        print_nodes(root.right)
    print({root.get_frequency()}, {root.get_data()})


