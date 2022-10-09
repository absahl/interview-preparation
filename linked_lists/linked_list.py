from linked_list_node import *

class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        self.insert_node_at_head(LinkedListNode(data))
        
    def insert_node_at_head(self, node):
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def insert_at_tail(self, node):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    def __str__(self):
        result = "["
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += "]"
        return result
