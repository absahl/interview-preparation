"""
Given an array of n objects colored white, red, or blue, sort the array in
place so that objects of the same color are adjacent, with the colors in the
order red, white, and blue.

This problem is known as Dutch National Flag Problem. The idea is to attribute
a color to each number and then arrange them following the order of colors on
the Dutch flag.

We'll use the integers 0, 1, and 2 to represent red, white, and blue,
respectively.

Sample input#
[2, 0, 2, 1, 1, 0]
Expected output#
[0, 0, 1, 1, 2, 2]
"""

def sort_colors(arr):
    """
    Sort colors in 2 iterations.
    In first iteration, sort between (0,1) and (2,) classes using two-array
    technique and in second iteration sort between 0 and 1 using the same
    technique.

    Time compexity: O(N)
    Space complexity: O(1)
    """
    print('arr: {0}'.format(arr))

    print(' sort class (0,1) to the left and (2,) to the right'.format(arr))
    i = 0
    j = len(arr) - 1
    print(' i: {0}, j: {1}'.format(i, j))
    while i < j:
        if arr[i] in (0, 1):
            i += 1
        elif arr[j] in (2,):
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    print(' array after first iteration: {0}'.format(arr))

    print(' sort 0 to the left and 1 to the right of remaining unsorted array'.format(arr))
    i = 0
    print(' i: {0}, j: {1}'.format(i, j))
    while i < j:
        if arr[i] in (0,):
            i += 1
        elif arr[j] in (1,):
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    print(' fully sorted: {0}'.format(arr))

def sort_colors_1(arr):
    print('arr: {0}'.format(arr))

    start = index = 0
    end = len(arr) - 1
    while index <= end:
        if arr[index] == 0:
            arr[start], arr[index] = arr[index], arr[start]
            index += 1
            start += 1
        elif arr[index] == 2:
            arr[index], arr[end] = arr[end], arr[index]
            end -= 1
        else:
            index += 1

    print(' sorted: {0}'.format(arr))

if __name__ == '__main__':
    sort_colors_1([2, 0, 2, 1, 1, 0])
    sort_colors_1([])
    sort_colors_1([2, 0, 1])
    sort_colors_1([2, 0, 2, 1, 1, 0])
    sort_colors_1([2, 0, 2, 1, 1, 0, 1, 0, 1, 0, 2])
    sort_colors_1([0, 0, 0])
