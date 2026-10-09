from linked_list import LinkedList
class OrderQueue:
    '''order queue class'''
    def __init__(self, l=None):
        '''order queue init'''
        self.LL = LinkedList(l)

    def enqueue(self, item):
        '''enqueue an item to the end of the list'''
        self.LL.add_last(item=item)

    def dequeue(self):
        '''dequeue an item from the front of the list and return it'''
        return self.LL.remove_first()

    def peek(self):
        '''look at the first item in the list'''
        return self.LL.get_first()

    def is_empty(self):
        '''check if the list is empty'''
        return self.LL.is_empty()

    def size(self):
        '''check the size of the list'''
        return self.LL.size()