"""
Remove duplicate nodes from a linked list of integers, retaining only the first
occurrence of each duplicate.

Given a linked list of integers, remove all the duplicate nodes from the linked
list while retaining only the first occurrence of each duplicate.

Sample input#
[4, 7, 4, 9, 7, 11, 4]
Expected output#
[4, 7, 9, 11]
"""

from linked_list_node import LinkedListNode
from linked_list import LinkedList

def remove_duplicates(head):
    """
    Time compexity: O(N)
    Space complexity: O(N)
    """

    hashset = set()
    node = head
    parent = None
    while node is not None:
        if node.data in hashset:
            node = node.next
            parent.next = node
        else:
            hashset.add(node.data)
            parent = node
            node = node.next

    return head

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.create_linked_list([4, 7, 4, 9, 7, 11, 4])
    linked_list.head = remove_duplicates(linked_list.head)
    assert str(linked_list) == '[4, 7, 9, 11]'
    print('[4, 7, 4, 9, 7, 11, 4] test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([-1, 2, 3, 4, 2, 2, 3, 4])
    linked_list.head = remove_duplicates(linked_list.head)
    assert str(linked_list) == '[-1, 2, 3, 4]'
    print('[-1, 2, 3, 4, 2, 2, 3, 4] test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([10])
    linked_list.head = remove_duplicates(linked_list.head)
    assert str(linked_list) == '[10]'
    print('[10] test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5])
    linked_list.head = remove_duplicates(linked_list.head)
    assert str(linked_list) == '[1, 2, 3, 4, 5]'
    print('[1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5] test successful')

    linked_list = LinkedList()
    linked_list.create_linked_list([28, -1, 21, 14, 7, -1])
    linked_list.head = remove_duplicates(linked_list.head)
    assert str(linked_list) == '[28, -1, 21, 14, 7]'
    print('[28, -1, 21, 14, 7, -1] test successful')
