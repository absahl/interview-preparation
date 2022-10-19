"""
Given the head pointer of a linked list, sort the linked list in ascending
order using merge sort and return the new head pointer of the sorted linked
list.

Sample input#
[29, 23, 82, 11, 4, 3, 21]
Expected output#
[3, 4, 11, 21, 23, 29, 82]
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

def merge_sort(head):
    """
    Time complexity: O(NLogN)
    Space complexity: O(1)
    """

    if head is None or head.next is None:
        return head

    # find the middle node parent O(N),O(1)
    trailing = head
    leading = head.next
    while leading and leading.next:
        leading = leading.next.next
        trailing = trailing.next

    # decouple the two lists
    parent = trailing
    trailing = trailing.next
    parent.next = None

    # sort the decoupled lists separately O(LogN),O(1)
    head = merge_sort(head)
    trailing = merge_sort(trailing)

    # merge the sorted lists O(N),O(1)
    merged = merge_sorted(head, trailing)

    return merged

if __name__ == '__main__':
    test_inputs = (
        [29, 23, 82, 11, 4, 3, 21],
        [7, 3, 2, 8, 5],
        [1, 2, 3, 7, 4, 5, 9],
        [33, 2, 11, 44, 24],
        [33, 2, 11, 44, 24]
    )

    expected_outputs = (
        [3, 4, 11, 21, 23, 29, 82],
        [2, 3, 5, 7, 8],
        [1, 2, 3, 4, 5, 7, 9],
        [2, 11, 24, 33, 44],
        [2, 11, 24, 33, 44]
    )

    assert len(test_inputs) == len(expected_outputs)

    for i in range(len(test_inputs)):
        print('test#{0} - {1}'.format(i + 1, test_inputs[i]))

        linked_list = LinkedList()
        linked_list.create_linked_list(test_inputs[i])
        print(' input: {0}'.format(str(linked_list)))
        linked_list.head = merge_sort(linked_list.head)
        print(' output: {0}'.format(str(linked_list)))
        assert str(linked_list) == str(expected_outputs[i])
        print(' successful'.format(input))
