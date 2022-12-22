import frequency_list
import heapq
class MinHeap:
    items = []

    def _get_left_child_index(self, parentindex):
        return 2 * parentindex + 1

    def getrightchildindex(self, parentindex):
        return 2 * parentindex + 2

    def getparentindex(self, childindex):
        return int((childindex - 1)/2)

    def hasleftchild(self, index):
        return self.getleftchildindex(index) < self.items.count()

    def hasrightchild(self, index):
        return self.getrightchildindex(index) < self.items.count()

    def hasparent(self, index):
        return self.getparentindex(index) >= 0

    def leftchild(self, index):
        return self.items[self.getleftchildindex(index)]

    def rightchild(self, index):
        return self.items[self.getrightchildindex(index)]

    def parent(self, index):
        return self.items[self.getparentindex(index)]

    def swap(self, index1, index2):
        temp = self.items[index1]
        self.items[index1] = self.items[index2]
        self.items[index2] = temp

    def peek(self):
        if len(self.items) == 0:
            return "List is empty"
        else:
            return items[0]

    def poll(self):
        if len(self.items) == 0:
            return "List is empty"
        else:
            item = self.items[0]
            self.items[0] = self.items[len(self.items) - 1]
            self.items.pop(len(self.items) - 1)
            self.heapifydown()
            return item

    def add(self, item):
        self.items.append(item)
        self.heapifyup()
        print(self.items)

    def heapifyup(self):
        index = len(self.items) - 1
        while self.hasparent(index) and (self.items[self.getparentindex(index)] > self.items[index]):
            self.swap(index, self.getparentindex(index))
            index = self.getparentindex(index)

    def heapifydown(self):
        index = 0
        while self.hasleftchild(index):
            smallchildindex = self.getleftchildindex(index)
            if self.hasrightchild(index) and self.rightchild(index) < self.leftchild(index):
                smallchildindex = self.getrightchildindex(index)
            if self.items[index] > items[smallchildindex]:
                self.swap(index, smallchildindex)
            index = smallchildindex




frequency_queue = MinHeap()
dict = frequency_list.letter_freq
for item in dict.values():
    frequency_queue.add(item)

print(frequency_queue.item)












