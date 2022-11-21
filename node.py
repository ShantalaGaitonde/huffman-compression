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

    def generate_huffmantree(self, li):
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


