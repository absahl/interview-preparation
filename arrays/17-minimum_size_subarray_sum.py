"""
Given an array of integers and a target, return the length of the shortest
contiguous subarray whose sum is greater than or equal to the target.

Given an array of positive integers, nums, along with a positive integer,
target. Find the length of the shortest contiguous subarray whose sum is
greater than or equal to the target. If there is no such subarray, return 0
instead.

Sample input#
target = 7
nums = [2,3,1,2,4,3]
Expected output#
2
"""

def min_sub_array_len(target, nums):
    """
    Time complexity: O(N^2)
    Space complexity: O(1)
    """

    print('nums: {0}, target: {1}'.format(nums, target))
    nums_len = len(nums)

    if sum(nums) < target:
        print(' sum of nums is smaller than target - return 0')
        return 0

    result = nums_len
    for i in range(nums_len):
        temp_sum = 0
        for j in range(i, nums_len):
            temp_sum += nums[j]
            #print(' i: {0}, j: {1}, temp_sum: {2}'.format(i, j, temp_sum))
            if temp_sum >= target and (j - i + 1) < result:
                result = j - i + 1
                #print(' updated result: {0}'.format(result))
                break

    print(' result: {0}'.format(result))
    return result

def min_sub_array_len_1(target, nums):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

    print('nums: {0}, target: {1}'.format(nums, target))
    nums_len = len(nums)

    if sum(nums) < target:
        print(' sum of nums is smaller than target - return 0')
        return 0

    left = right = 0
    temp_sum = 0
    result = nums_len
    while left < nums_len and right < nums_len:
        temp_sum += nums[right]
        if temp_sum >= target:
            #print(' target reached between {0} and {1}'.format(left, right))
            if (right + 1 - left) < result:
                result = right + 1 - left
                #print(' updated result: {0}'.format(result))

            #print(' before remaining sum: {0}'.format(temp_sum))
            temp_sum -= (nums[left] + nums[right])
            #print(' remaining sum: {0}'.format(temp_sum))
            left += 1
            if right < left:
                right = left
        else:
            right += 1

    print(' result: {0}'.format(result))
    return result

if __name__ == '__main__':
    assert min_sub_array_len_1(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_sub_array_len_1(4, [1, 4, 4]) == 1
    assert min_sub_array_len_1(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert min_sub_array_len_1(6, [5, 2]) == 2
    assert min_sub_array_len_1(2, [0, 0, 1, 0, 1]) == 3
    assert min_sub_array_len_1(3, [1, 0, 1, 0, 1]) == 5
