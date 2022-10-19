"""
Given two sorted linked lists, merge them so that the resulting linked list is
also sorted.

Sample input#
[4, 8, 15, 19, 22]
[7, 9, 10, 16]
Expected output#
[4, 7, 8, 9, 10, 15, 16, 19, 22]
"""

from linked_list_node import LinkedListNode
from linked_list import LinkedList

def merge_sorted(head1, head2):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    result = None
    if head1.data < head2.data:
        result = head1
        head1 = head1.next
    else:
        result = head2
        head2 = head2.next

    parent = result
    while head1 or head2:
        if head1 and head2:
            if head1.data < head2.data:
                parent.next = head1
                head1 = head1.next
            else:
                parent.next = head2
                head2 = head2.next
        elif head1:
            parent.next = head1
            head1 = head1.next
        else:
            parent.next = head2
            head2 = head2.next

        parent = parent.next

    parent.next = None
    return result

if __name__ == '__main__':
    test_inputs = (
        ([], []),
        ([], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], []),
        ([1, 2, 3, 4, 5], [10, 20, 30, 40, 50]),
        ([29, 39, 49, 69], [6, 7, 8, 9, 10]),
        ([4, 8, 15, 19, 22], [7, 9, 10, 16])
    )

    expected_outputs = (
        [],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 10, 20, 30, 40, 50],
        [6, 7, 8, 9, 10, 29, 39, 49, 69],
        [4, 7, 8, 9, 10, 15, 16, 19, 22]
    )

    assert len(test_inputs) == len(expected_outputs)

    for i in range(len(test_inputs)):
        print('test#{0} - {1}'.format(i + 1, test_inputs[i]))

        linked_list_1 = LinkedList()
        linked_list_1.create_linked_list(test_inputs[i][0])
        linked_list_2 = LinkedList()
        linked_list_2.create_linked_list(test_inputs[i][1])
        print(' input: {0} and {1}'.format(str(linked_list_1), str(linked_list_2)))
        linked_list_1.head = merge_sorted(linked_list_1.head, linked_list_2.head)
        print(' output: {0}'.format(str(linked_list_1)))
        assert str(linked_list_1) == str(expected_outputs[i])
        print(' successful'.format(input))
