"""
Given an array of integers, find the arrangement that yields the largest number.

Given an array of integers, find the largest number that can be made by
creating all possible permutations of these integers.

As the largest number formed can be very large, Return a string instead of an
integer.

Sample input#
[3, 30, 34, 5, 9]
Expected output#
"9534330"
"""

def quick_sort_descending(nums, low=None, high=None, context=''):
    low = 0 if low is None else low
    high = len(nums) - 1 if high is None else high
    if high <= low:
        return

    index = low
    for i in range(low, high):
        if nums[i]+nums[high] > nums[high]+nums[i]:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1

    nums[index], nums[high] = nums[high], nums[index]

    quick_sort_descending(nums, low, index - 1, context + ' ')
    quick_sort_descending(nums, index + 1, high, context + ' ')

def largest_number(nums):
    """
    Convert integer array to string array.
    Run quick sort in reverse order. Criteria of bigger number between two
    numbers is the one which gives bigger number after concatenation.
    At last, concatenate the strings together unless first element is 0.
    0 means all following elements are also 0's.

    Time complexity: O((N*LogN)
    Space complexity: O((N*LogN)
    """

    print('nums: {0}'.format(nums))
    nums = [str(s) for s in nums] # O(N)

    quick_sort_descending(nums, context=' ') #O(N*LogN) O(N*LogN)
    print(' sorted nums: {0}'.format(nums))

    if len(nums) > 0 and nums[0] == '0':
        result = '0'
    else:
        result = ''.join(nums)

    print(' result: {0}'.format(result))
    return result

class SortingOrderDecider(str):
    def __lt__(s1, s2):
        return s1+s2 < s2+s1

def largest_number_1(arr):
    """
    Above method using pythonic way
    """

    print('arr: {0}'.format(arr))

    sorted_arr_str = sorted(map(str, arr), key=SortingOrderDecider, reverse=True)
    print(' sorted arr str: {0}'.format(sorted_arr_str))

    result = ''.join(sorted_arr_str)
    if len(result) > 0 and result[0] == '0':
        result = '0'

    print(' result: {0}'.format(result))
    return result

if __name__ == '__main__':
    largest_number_1([3, 30, 34, 5, 9])
    largest_number_1([95, 34, 30, 3])
    largest_number_1([10, 20])
    largest_number_1([21, 6])
    largest_number_1([0, 0])
    largest_number_1([6, 7])
    largest_number_1([3, 30, 34, 5, 7])
    largest_number_1([25, 35, 45, 55, 51])
    largest_number_1([2, 5, 9, 14, 20, 21, 10, 26, 28])
    largest_number_1([10, 20, 30, 40, 50, 60, 70, 80, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9])
