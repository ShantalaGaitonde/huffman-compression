from bitarray import bitarray
huffman_code_dict = {}


def generate_codes(root, str1):
    str1 = str1 + root.code
    if root.left is not None:
        generate_codes(root.left, str1)
    if root.right is not None:
        generate_codes(root.right, str1)
    if root.get_data() is not None:
        arr = bitarray(str1)
        huffman_code_dict.update({root.get_data(): arr})
        str1 = ""
    return huffman_code_dict
