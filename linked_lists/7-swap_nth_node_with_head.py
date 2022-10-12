"""
Given the head of a singly linked list and 'n', swap the head with the nth
node. Return the head of the new linked list.

Sample input#
[28, 21, 14, 7]
n = 4
Expected output#
[7, 21, 14, 28]
"""

from linked_list_node import LinkedListNode
from linked_list import LinkedList

def swap_nth_node(head, n):
    """
    Time complexity: O(N) , N being minimum between n and length of linked list
    Space complexity: O(1)
    """

    if n <= 1 or head is None:
        return head

    parent = head
    count = n - 2
    while parent.next and count > 0:
        parent = parent.next
        count -= 1

    if parent.next:
        new_head = parent.next
        parent.next = head
        head_next = head.next
        head.next = new_head.next
        new_head.next = head_next
        head = new_head

    return head

if __name__ == '__main__':
    test_inputs = (
        ([-1, 2, 3, 4], 1),
        ([10], 2),
        ([1, 1, 2, 3, 4, 5], 3),
        ([28, 21, 14, 7], 4),
        ([1, 2, 3, 4, 5, 6], 6),
        ([1, 2, 3, 4, 5, 6], 7)
    )

    expected_outputs = (
        [-1, 2, 3, 4],
        [10],
        [2, 1, 1, 3, 4, 5],
        [7, 21, 14, 28],
        [6, 2, 3, 4, 5, 1],
        [1, 2, 3, 4, 5, 6]
    )

    assert len(test_inputs) == len(expected_outputs)

    for i in range(len(test_inputs)):
        print('test#{0} - {1}'.format(i + 1, test_inputs[i]))

        linked_list = LinkedList()
        linked_list.create_linked_list(test_inputs[i][0])
        print(' input: {0}'.format(str(linked_list)))
        linked_list.head = swap_nth_node(linked_list.head, test_inputs[i][1])
        print(' output: {0}'.format(str(linked_list)))
        assert str(linked_list) == str(expected_outputs[i])
        print(' successful'.format(input))
