"""
Given a singly linked list, return the nth node from the last node. Return null
if n is larger than the size of the list.

We're given a singly linked list. Return the nth node from the last node.
Return null if n is larger than the size of the list.

Sample input#
[1, 1, 2, 3, 4, 5]
n = 3
Expected output#
3
"""

from linked_list_node import LinkedListNode
from linked_list import LinkedList

def find_nth_from_last(head, n):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

    if n < 1:
        return None

    left = None
    right = head
    count = 0
    while right:
        right = right.next
        count += 1

        if left:
            left = left.next
        elif count >= n:
            left = head

    return left

if __name__ == '__main__':
    test_inputs = (
        ([-1, 2, 3, 4], 1),
        ([10], 2),
        ([1, 1, 2, 3, 4, 5], 3),
        ([28, 21, 14, 7], 4),
        ([1, 2], 0),
        ([1, 2, 3, 4, 5, 6], 6)
    )

    expected_outputs = (
        4,
        None,
        3,
        28,
        None,
        1
    )

    assert len(test_inputs) == len(expected_outputs)

    for i in range(len(test_inputs)):
        print('test#{0} - {1}'.format(i + 1, test_inputs[i]))

        linked_list = LinkedList()
        linked_list.create_linked_list(test_inputs[i][0])
        print(' input: {0}'.format(str(linked_list)))
        result = find_nth_from_last(linked_list.head, test_inputs[i][1])
        print(' result: {0}'.format(result))
        assert str(result) == str(expected_outputs[i])
        print(' successful'.format(input))
