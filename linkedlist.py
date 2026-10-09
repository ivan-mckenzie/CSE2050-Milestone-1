from typing import Any, Optional


class Node:
    """node class"""
    def __init__(self, item: Any, link: "Node | None" = None) -> None:
        """intis a node"""
        self.item = item
        self.link = link    


class LinkedList:
    """linked list class"""
    def __init__(self, items=None):
        """inits a linkedlist"""
        self._head = None
        self._tail = None
        self._len = 0

        if items is not None:
            for item in items:
                self.add_last(item)

    def is_empty(self):
        '''returns true if list is empty and false otherwise'''
        return not len(self)

    def size(self):
        """length of linkedlist"""
        return self._len

    def __len__(self):
        """length of linkedlist"""
        return self._len

    def get_first(self):
        """gets the first item in the linked list"""
        if self._head is not None:
            return self._head.item

    def add_last(self, item):
        '''adds item to the tail of the linked list'''

        node = Node(item, link=None)
        if len(self) == 0:
            self._head = node
        else:
            self._tail.link = node

        self._tail = node
        self._len += 1

    def add_first(self, item):
        '''adds item to the head of the linked list'''
        if len(self) == 0:
            self.add_last(item)
        else:
            node = Node(item, link=self._head)

            self._head = node
            self._len += 1

    def remove_first(self):
        '''removes node at the head of the linked list'''
        if len(self) == 0:
            return None

        ret = self.get_head()

        if len(self) == 1:
            self._head = self._tail = None
        else:
            self._head = self._head.link

        self._len -= 1
        return ret

