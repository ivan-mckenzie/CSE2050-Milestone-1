from linked_list import LinkedList

class Stack:
    '''stack class'''
    def __init__(self, l=None):
        '''init a stack class'''
        self.LL = LinkedList(l)

    def push(self, item):
        '''push an item to the front of the stack'''
        self.LL.add_first(item=item)

    def pop(self):
        '''pop an item from the top of the stack'''
        return self.LL.remove_first()

    def peek(self):
        '''peek at the top of the stack'''
        return self.LL.get_first()

    def is_empty(self):
        '''check if stack is empty'''
        return self.LL.is_empty()

    def size(self):
        '''return the size of the stack'''
        return self.LL.size()