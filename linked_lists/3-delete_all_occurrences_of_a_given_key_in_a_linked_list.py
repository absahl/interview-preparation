"""
Given the head of a linked list and a key, delete all nodes whose values match
the given key.

We're given the head of a linked list and a key. Delete all the nodes that
contain the given key.
Note: The input linked list will not have cycles in it.

Sample input#
[20, 14, 36, 11, 72, 41]
key = 72
Expected output#
[20, 14, 36, 11, 41]
"""

from linked_list_node import LinkedListNode
from linked_list import LinkedList

def delete_node(head, key):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

    node = head
    parent = None
    while node is not None:
        if node.data != key:
            parent = node
            node = node.next
            continue

        if node is head:
            node = head = head.next
        else:
            parent.next = node.next
            node = parent.next

    return head

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.create_linked_list([20, 14, 36, 11, 72, 41])
    linked_list.head = delete_node(linked_list.head, 72)
    assert str(linked_list) == '[20, 14, 36, 11, 41]'
    print('[20, 14, 36, 11, 72, 41], 72 test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([10, 20, -22, 21, -12, -12])
    linked_list.head = delete_node(linked_list.head, 12)
    assert str(linked_list) == '[10, 20, -22, 21, -12, -12]'
    print('[10, 20, -22, 21, -12, -12], 12 test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([10, 10, 10])
    linked_list.head = delete_node(linked_list.head, 10)
    assert str(linked_list) == '[]'
    print('[10, 10, 10], 10 test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([-1])
    linked_list.head = delete_node(linked_list.head, -1)
    assert str(linked_list) == '[]'
    print('[-1], -1 test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([4, 6, 54, 20, 1])
    linked_list.head = delete_node(linked_list.head, 4)
    assert str(linked_list) == '[6, 54, 20, 1]'
    print('[4, 6, 54, 20, 1], 4 test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([1, 2, 3, 4])
    linked_list.head = delete_node(linked_list.head, 1)
    assert str(linked_list) == '[2, 3, 4]'
    print('[1, 2, 3, 4], 1 test successful')
