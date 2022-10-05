"""
We're given an array of integers and a value.
Determine if there are any two integers in the array whose sum is equal to the given value.
Return true if the sum exists; otherwise, return false.
"""

def find_sum_of_two(nums, val):
    """
    time complexity: O(N * Log(N))
    space complexity: O(1)
    """
    print('nums: {0}, val: {1}'.format(nums, val))

    nums.sort()
    print(' sorted nums: {0}'.format(nums))

    left = 0
    right = len(nums) - 1
    while left < right:
        left_right_sum = nums[left] + nums[right]
        if left_right_sum == val:
            print(' sum found at {0} and {1}'.format(left, right))
            return True
        elif left_right_sum < val:
            left += 1
        else:
            right -= 1

    print(' sum not found')
    return False

def find_sum_of_two_1(nums, val):
    """
    time complexity: O(N)
    space complexity: O(N)
    """
    print('nums: {0}, val: {1}'.format(nums, val))

    lookup_set = set()
    for i in range(0, len(nums)):
        if (val - nums[i]) in lookup_set:
            print(' sum found')
            return True

        lookup_set.add(nums[i])

    print(' sum not found')
    return False

if __name__ == '__main__':
    find_sum_of_two_1([2, 1, 8, 4, 7, 3], 3)
    find_sum_of_two_1([1, 2, 3, 4, 7, 8], 20)
    find_sum_of_two_1([1, 2, 3, 4, 7, 8], 7)
    find_sum_of_two_1([1, 2, 3, 4, 7, 8], 2)
    find_sum_of_two_1([1, 2, 3, 4, 7, 8], 12)
    find_sum_of_two_1([1, 2, 3, 4, 7, 8], 10)
    find_sum_of_two_1([1, 2, 3, 4, 7, 8], 11)
