from bitarray import bitarray
import heapq


class Node:
    def __init__(self, data, frequency):
        self.left = None
        self.right = None
        self.data = data
        self.frequency = frequency
        self.code = ''

    def increment_count(self):
        self.frequency = self.get_frequency() + 1

    def get_data(self):
        return self.data

    def get_frequency(self):
        return self.frequency

    def __lt__(self, nxt):
        return self.frequency < nxt.frequency

    def has_left(self):
        if self.left is None:
            return False
        else:
            return True

    def has_right(self):
        if self.right is None:
            return False
        else:
            return True


def generate_codes(huffman_code_dict, root, str1):
    str1 = str1 + root.code
    if root.left is not None:
        generate_codes(huffman_code_dict, root.left, str1)
    if root.right is not None:
        generate_codes(huffman_code_dict, root.right, str1)
    if root.get_data() is not None:
        arr = bitarray(str1)
        huffman_code_dict.update({root.get_data(): arr})


def generate_frequency_dictionary(text):
    letter_freq = {}
    for c in range(0, len(text)):
        if letter_freq.get(text[c]) is None:
            newnode = Node(text[c], 1)
            letter_freq.update({text[c]: newnode})
        else:
            node = letter_freq.get(text[c])
            node.increment_count()
    return letter_freq


def heapify(letter_freq):
    li = []
    print("The huffman tree is\n")
    heapq.heapify(li)
    for value in letter_freq.values():
        heapq.heappush(li, value)
    return li


def generate_huffmantree(freqeuency_table):
    li = heapify(freqeuency_table)
    while len(li) > 1:
        node1 = heapq.heappop(li)
        node2 = heapq.heappop(li)
        root = Node(None, node1.get_frequency() + node2.get_frequency())
        if node1.get_frequency() < node2.get_frequency():
            node1.code = "0"
            node2.code = "1"
            root.left = node1
            root.right = node2
        else:
            node1.code = "1"
            node2.code = "0"
            root.left = node2
            root.right = node1
        heapq.heappush(li, root)
    return root