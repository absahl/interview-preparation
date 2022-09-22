"""
We're given three integer arrays, each sorted in ascending order.
Return the smallest number common in all three arrays.
In case no number is common, return -1.
"""

from collections import OrderedDict

def find_next_index(arr, current_index):
    next_index = current_index + 1
    while next_index < len(arr) and arr[next_index] == arr[current_index]:
        next_index += 1

    return next_index

def find_least_common_number(arr1, arr2, arr3):
    #print('arr1: {0}, arr2: {1}, arr3: {2}'.format(arr1, arr2, arr3))

    arr1_len = len(arr1)
    arr2_len = len(arr2)
    arr3_len = len(arr3)

    i = 0
    j = 0
    k = 0
    a_dict = OrderedDict()
    while i < arr1_len or j < arr2_len or k < arr3_len:
        if i < arr1_len:
            a_dict[arr1[i]] = a_dict.get(arr1[i], 0) + 1
            i = find_next_index(arr1, i)
        if j < arr2_len:
            a_dict[arr2[j]] = a_dict.get(arr2[j], 0) + 1
            j = find_next_index(arr2, j)
        if k < arr3_len:
            a_dict[arr3[k]] = a_dict.get(arr3[k], 0) + 1
            k = find_next_index(arr3, k)

    print(' a_dict: {0}'.format(a_dict))

    result = -1
    for k in a_dict:
        if a_dict[k] == 3:
            result = k
            break

    print(' result: {0}'.format(result))
    return result

def find_least_common_number(arr1, arr2, arr3):
    print('arr1: {0}, arr2: {1}, arr3: {2}'.format(arr1, arr2, arr3))

    i = 0
    j = 0
    k = 0
    result = -1
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        print(' i: {0} [{1}], j: {2} [{3}], k: {4} [{5}]'.format(i, arr1[i], j, arr2[j], k, arr3[k]))
        if arr1[i] == arr2[j] == arr3[k]:
            result = arr1[i]
            break

        if arr1[i] <= arr2[j] and arr1[i] <= arr3[k]:
            i += 1
        elif arr2[j] <= arr1[i] and arr2[j] <= arr3[k]:
            j += 1
        else:
            k += 1

    print(' result: {0}'.format(result))
    return result

if __name__ == '__main__':
    find_least_common_number([6, 7, 10, 25, 30, 63, 64], [0, 4, 5, 6, 7, 8, 50], [1, 6, 10, 14])
    find_least_common_number([1, 4, 6, 7, 8, 10, 14], [1, 4, 5, 6, 7, 8, 50], [0, 6, 7, 8, 10, 25, 30, 40])
