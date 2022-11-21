import heapq
from node import Node
letter_freq = {}


def generate_frequency_dictionary(text):
    for c in range(0, len(text)):
        if letter_freq.get(text[c]) is None:
            newnode = Node(text[c], 1)
            letter_freq.update({text[c]: newnode})
        else:
            node = letter_freq.get(text[c])
            node.increment_count()
    return letter_freq
