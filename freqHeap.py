import heapq

import decodeFile
import frequency_list
import huffmanCode
import encodeFile


# Huffman Coding in python
from tkinter.filedialog import askopenfilename
filetypes = (
    ('Text files', '*.TXT'),
    ('All files', '*.*'),
)

filename = askopenfilename(
    filetypes=filetypes,)

text_file = open(filename, "r")
text = text_file.read()
text_file.close()
print("The text to be encoded is \n" + text)
letter_freq = frequency_list.generate_frequency_dictionary(text)
li = []
print("The huffman tree is\n")
heapq.heapify(li)
for value in letter_freq.values():
    heapq.heappush(li, value)
print(li)
root = li[0].generate_huffmantree(li)


def print_nodes(root):
    if root.left is not None:
        print_nodes(root.left)
    if root.right is not None:
        print_nodes(root.right)
    print({root.get_frequency()}, {root.get_data()})



str1 = ""
print("The huffman tree nodes are \n")
print_nodes(root)
print("The huffman code dictionary is\n")
print(huffmanCode.generate_codes(root, str1))
encoded_file, padded_bits = encodeFile.huffman_encode(filename, huffmanCode.generate_codes(root, str1))
decodeFile.huffman_decode(encoded_file, huffmanCode.generate_codes(root, str1), padded_bits)















