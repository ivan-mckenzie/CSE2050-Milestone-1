from linked_list import LinkedList

class Stack:

    def __init__(self, l=None):
        self.LL = LinkedList(l)

    def push(self, item):
        self.LL.add_first(item=item)

    def pop(self):
        return self.LL.remove_first()

    def peek(self):
        return self.LL.get_first()

    def is_empty(self):
        return self.LL.is_empty()

    def size(self):
        return self.LL.size()