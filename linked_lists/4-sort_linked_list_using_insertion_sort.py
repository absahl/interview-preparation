"""
Given the head pointer of a linked list, sort it in ascending order using
insertion sort.

We're given the head pointer of a linked list. Sort the linked list in
ascending order using insertion sort. Return the new head pointer of the sorted
linked list.

Sample input#
[29, 23, 82, 11]
Expected output#
[11, 23, 29, 82]
"""

from linked_list_node import LinkedListNode
from linked_list import LinkedList

def insertion_sort(head):
    """
    Time complexity: O(N^2)
    Space complexity: O(1)
    """

    node = head
    while node:
        inner_node = head
        while inner_node and inner_node is not node:
            if inner_node.data > node.data:
                inner_node.data, node.data = node.data, inner_node.data
            inner_node = inner_node.next
        node = node.next

    return head

if __name__ == '__main__':
    test_inputs = (
        [29, 23, 82, 11],
        [5, 2, 3, 1, 4],
        [10],
        [100, 120, 90, 1],
        [-1, -10, 20],
        [9, 7, -2, 10],
        [14, 13, 12, 11],
        [29, 23, 82, 11]
    )

    expected_outputs = (
        [11, 23, 29, 82],
        [1, 2, 3, 4, 5],
        [10],
        [1, 90, 100, 120],
        [-10, -1, 20],
        [-2, 7, 9, 10],
        [11, 12, 13, 14],
        [11, 23, 29, 82]
    )

    assert len(test_inputs) == len(expected_outputs)

    for i in range(len(test_inputs)):
        print('test#{0} - {1}'.format(i + 1, test_inputs[i]))

        linked_list = LinkedList()
        linked_list.create_linked_list(test_inputs[i])
        print(' input: {0}'.format(str(linked_list)))
        linked_list.head = insertion_sort(linked_list.head)
        print(' output: {0}'.format(str(linked_list)))
        assert str(linked_list) == str(expected_outputs[i])
        print(' successful'.format(input))
