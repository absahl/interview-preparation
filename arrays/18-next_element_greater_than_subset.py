"""
Find the next greater element for each value in the subset array.

Given two integer arrays, nums1 and nums2, where nums1 is a subset of nums2,
find the next greater element of some element x in nums2 that is to the right
of x in the same array. If there is no next greater element, then the answer is
-1.

Constraints#
1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 10000
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.
"""

def next_greater_element(nums1, nums2):
    """
    Time complexity: O(N1 * N2) ~ O(N^2)
    Space complexity: O(1)
    """

    print('nums1: {0}, nums2: {1}'.format(nums1, nums2))

    for i in range(len(nums1)):
        print(' finding next greater of {0}'.format(nums1[i]))

        key_result = -1
        j = len(nums2) - 1
        while nums2[j] != nums1[i]:
            #print(' checking {0}'.format(nums2[j]))
            if nums2[j] > nums1[i]:
                key_result = nums2[j]

            j -= 1

        print(' key result: {0}'.format(key_result))
        nums1[i] = key_result

    print(' result: {0}'.format(nums1))
    return nums1

def next_greater_element_1(nums1, nums2):
    """
    Time complexity: O(N)
    Space complexity: O(N)
    """

    print('nums1: {0}, nums2: {1}'.format(nums1, nums2))
    stack = []
    hashmap = {}

    i = 0
    while i < len(nums2):
        if not stack or stack[-1] > nums2[i]:
            stack.append(nums2[i])
            i += 1
        else:
            hashmap[stack.pop()] = nums2[i]

    print(stack, hashmap)

    while stack:
        hashmap[stack.pop()] = -1

    print(hashmap)

    nums1 = [hashmap[i] for i in nums1]
    print(' result: {0}'.format(nums1))
    return nums1

if __name__ == '__main__':
    assert next_greater_element_1([4, 1, 2], [1, 3, 4, 2]) == [-1, 3, -1]
    assert next_greater_element_1([2, 4], [1, 2, 3, 4]) == [3, -1]
    assert next_greater_element_1([3, 0, 1], [2, 3, 5, 1, 0, 7]) == [5, 7, 7]
    assert next_greater_element_1([1, 2], [5, 2, 4, 1]) == [-1, 4]
    assert next_greater_element_1([2, 3, 4, 5], [7, 6, 5, 4, 3, 2]) == [-1, -1, -1, -1]
    assert next_greater_element_1([3, 7, 0, 1], [2, 3, 5, 1, 0, 7]) == [5, -1, 7, 7]
