"""
Given a singly linked list, reverse the nodes at even positions.

Sample input#
[7, 14, 21, 28, 9]
Expected output#
[7, 28, 21, 14, 9]
"""

from linked_list import LinkedList

def get_nodes(head):
    node = head
    a_list = []
    while node:
        a_list.append(node.data)
        node = node.next

    return a_list

def reverse(head):
    node = head
    parent = None
    while node:
        next_node = node.next
        node.next = parent
        parent = node
        node = next_node

    return parent

def reverse_even_nodes(head):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

    # separate linked list for even nodes
    even = None
    even_curr = None
    curr = head
    while curr and curr.next:
        if even is None:
            even = curr.next
            even_curr = even
        else:
            even_curr.next = curr.next
            even_curr = even_curr.next

        curr.next = even_curr.next
        curr = curr.next
        even_curr.next = None

    print(' odd: {0}, even: {1}'.format(get_nodes(head), get_nodes(even)))

    # reverse the even linked list
    even = reverse(even)
    print(' reverse even: {0}'.format(get_nodes(even)))

    # merge both lists
    print(' merging {0} and {1}'.format(get_nodes(head), get_nodes(even)))
    odd_curr = head
    even_curr = even
    while odd_curr and even_curr:
        temp = odd_curr.next
        odd_curr.next = even_curr
        even_curr = even_curr.next
        odd_curr.next.next = temp
        odd_curr = temp

    return head

if __name__ == '__main__':
    test_inputs = (
        [7, 28, 21, 14, 9],
        [7, 14, 21, 28, 9],
        [0, 33, 21, 18],
        [7, 1, 7],
        [1, 2],
        [8],
        [],
        [-1, 5, 3, 4, 0]
    )

    expected_outputs = (
        [7, 14, 21, 28, 9],
        [7, 28, 21, 14, 9],
        [0, 18, 21, 33],
        [7, 1, 7],
        [1, 2],
        [8],
        [],
        [-1, 4, 3, 5, 0]
    )

    assert len(test_inputs) == len(expected_outputs)

    for i in range(len(test_inputs)):
        print('test#{0} - {1}'.format(i + 1, test_inputs[i]))

        linked_list = LinkedList()
        linked_list.create_linked_list(test_inputs[i])
        print(' input: {0}'.format(str(linked_list)))
        linked_list.head = reverse_even_nodes(linked_list.head)
        print(' output: {0}'.format(str(linked_list)))
        assert str(linked_list) == str(expected_outputs[i])
        print(' successful'.format(input))
