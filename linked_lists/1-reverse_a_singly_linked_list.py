"""
Reverse the singly linked list and return the head of the reversed linked list.

Given the head of a singly linked list, reverse the linked list and return its
new or updated head.

Sample input#
[7, 14, 21, 28]
Expected output#
[28, 21, 14, 7]
"""

from linked_list_node import LinkedListNode
from linked_list import LinkedList

def reverse(head):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

    if head is None or head.next is None:
        return head

    node = head
    prev_node = None
    while node.next:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node

    node.next = prev_node
    return node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.create_linked_list([-1, 2, 3, 4])
    linked_list.head = reverse(linked_list.head)
    assert str(linked_list) == '[4, 3, 2, -1]'
    print('[-1, 2, 3, 4] test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([10])
    linked_list.head = reverse(linked_list.head)
    assert str(linked_list) == '[10]'
    print('[10] test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([1, 1, 2, 3, 4, 5])
    linked_list.head = reverse(linked_list.head)
    assert str(linked_list) == '[5, 4, 3, 2, 1, 1]'
    print('[1, 1, 2, 3, 4, 5] test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([28, 21, 14, 7])
    linked_list.head = reverse(linked_list.head)
    assert str(linked_list) == '[7, 14, 21, 28]'
    print('[28, 21, 14, 7] test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([11, 12, 13, 14])
    linked_list.head = reverse(linked_list.head)
    assert str(linked_list) == '[14, 13, 12, 11]'
    print('[11, 12, 13, 14] test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([1, 2])
    linked_list.head = reverse(linked_list.head)
    assert str(linked_list) == '[2, 1]'
    print('[1, 2] test successful')
