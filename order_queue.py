from linkedlist import LinkedList
class OrderQueue:

    def __init__(self, l=None):
        self.LL = LinkedList(l)

    def enqueue(self, item):
        self.LL.add_last(item=item)

    def dequeue(self):
        return self.LL.remove_first()

    def peek(self):
        return self.LL.get_first()

    def is_empty(self):
        return self.LL.is_empty()

    def size(self):
        return self.LL.size()