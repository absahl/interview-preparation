"""
Given the head of two linked lists, find out if they intersect and return the
point of intersection.

Given the head nodes of two linked lists, return the node at which the two
lists intersect. We will return null if we do not find any intersection between
the two linked lists.
Note: The input linked list will not have cycles in it.

Sample input#
[13, 4, 12, 27]
[29, 23, 82, 11, 12, 27]
Expected output#
12
"""

from linked_list_node import LinkedListNode
from linked_list import LinkedList

def find_linked_list_length(head):
    length = 0
    node = head
    while node:
        node = node.next
        length += 1

    return length

def move_head(head, length):
    for i in range(length):
        head = head.next

    return head

def intersect(head1, head2):
    length1 = find_linked_list_length(head1)
    length2 = find_linked_list_length(head2)
    if length1 > length2:
        head1 = move_head(head1, length1-length2)
        shared_length = (length1+length2) - length1
    elif length2 > length1:
        head2 = move_head(head2, length2-length1)
        shared_length = (length1+length2) - length2
    else:
        shared_length = length1

    result = None
    for i in range(shared_length):
        print(' head1: {0}, head2: {1}'.format(head1, head2))
        if head1 == head2:
            result = head1
            break

        head1 = head1.next
        head2 = head2.next

    return result

if __name__ == '__main__':
    test_inputs = (
        ([13, 4, 12, 27], [29, 23, 82, 11, 12, 27]),
        ([4, 9, 16, 25, 30, 18, 10], [25, 30, 18, 10]),
        ([4, 9, 16, 25, 30, 18, 10], [22, 11, 25, 30, 18, 10]),
        ([30, 32, 40], [85, 90, 76]),
        ([30, 32, 40], [30, 32, 40]),
        ([100, 200, 0, 25, 50], [0, 25, 50])
    )

    expected_outputs = (
        12,
        25,
        25,
        None,
        30,
        0
    )

    assert len(test_inputs) == len(expected_outputs)

    for i in range(len(test_inputs)):
        print('test#{0} - {1}'.format(i + 1, test_inputs[i]))

        linked_list_1 = LinkedList()
        linked_list_1.create_linked_list(test_inputs[i][0])
        linked_list_2 = LinkedList()
        linked_list_2.create_linked_list(test_inputs[i][1])
        print(' input: {0},{1}'.format(str(linked_list_1), str(linked_list_2)))
        intersection_head = intersect(linked_list_1.head, linked_list_2.head)
        print(' output: {0}'.format(str(intersection_head)))
        #assert str(intersection_head) == str(expected_outputs[i])
        #print(' successful')
