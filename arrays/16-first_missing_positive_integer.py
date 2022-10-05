"""
Given an array of integers, find the smallest missing positive integer.

Given an unsorted integer array, nums, find the smallest positive integer that
is missing from the array. Implement a solution that takes O(n) time and
constant space.

Sample input#
[1, 9, 14, 11, 7, 13]
Expected output#
2
"""

def first_missing_positive(nums):
    """
    For an array with length, n, missing positive integer should be in (1, n+1)
    range, inclusive.
    We need to track what numbers in the range exist and the others which do
    not. Base case i.e. 1 will either be validated or eliminated first. Then,
    all numbers which are <1 and >n will be converted to 1.
    We will use index to represent the number from 1 to n. For value part,
    sign part will denote if the number represented by index exists or not.

    Time complexity: O(N)
    Space complexity: O(1)
    """

    print('nums: {0}'.format(nums))
    nums_len = len(nums)

    # check default case i.e. 1
    if 1 not in nums:
        print(' 1 not found - return 1')
        return 1

    # replace all numbers which are <1 or >n to 1
    for i in range(nums_len):
        if nums[i] < 1 or nums[i] > nums_len:
            nums[i] = 1

    print(' nums (with modified invalid numbers): {0}'.format(nums))

    # mark the present integers with -ve sign on values of corresponding
    # indices. Use 1-based indexing
    for i in range(nums_len):
        j = abs(nums[i]) - 1 # target index
        nums[j] = -abs(nums[j])

    print(' nums (with markings): {0}'.format(nums))

    result = nums_len + 1
    for i in range(nums_len):
        if nums[i] > 0:
            result = i + 1
            break

    print(' result: {0}'.format(result))
    return result

if __name__ == '__main__':
    assert first_missing_positive([1, 9, 14, 11, 7, 13, 2]) == 3
    assert first_missing_positive([5, 8, 2, 7, 1, 6, 3]) == 4
    assert first_missing_positive([-3, -1, -4, -2, -5]) == 1
    assert first_missing_positive([-1, 5, 3, 6, 2, 1, 4, 8]) == 7
    assert first_missing_positive([7, 2, 3, 8, 4, 1, 6]) == 5
    assert first_missing_positive([-1, 3, 6, 4, 2, 5, 0]) == 1
