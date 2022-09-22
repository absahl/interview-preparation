"""
Given an integer array, sorted in non-decreasing order,
return an array of the squares of each number, sorted in non-decreasing order.
"""

def find_smallest_positive_integer(nums):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] < 0:
            low = mid + 1
        else:
            if mid == 0 or nums[mid - 1] < 0:
                return mid
            else:
                high = mid - 1

    return len(nums)

def sorted_squares(nums):
    print('nums: {0}'.format(nums))
    result = []

    right = find_smallest_positive_integer(nums)
    left = right - 1
    while left >= 0 or right < len(nums):
        left_square = right_square = -1
        if left >= 0:
            left_square = nums[left] ** 2
        if right < len(nums):
            right_square = nums[right] ** 2

        if (right_square == -1) or (left_square != -1 and left_square <= right_square):
            result.append(left_square)
            left -= 1
        else:
            result.append(right_square)
            right += 1

    print(' result: {0}'.format(result))
    return result

def sorted_squares_1(nums):
    print('nums: {0}'.format(nums))
    result = [None] * len(nums)

    left = 0
    right = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) >= abs(nums[right]):
            result[i] = nums[left] * nums[left]
            left += 1
        else:
            result[i] = nums[right] * nums[right]
            right -= 1

    print(' result: {0}'.format(result))
    return result

if __name__ == '__main__':
    sorted_squares_1([-4, -1, 0, 3, 10])
    sorted_squares_1([-7, -3, 2, 3, 11])
    sorted_squares_1([-100, 100])
    sorted_squares_1([-5])
    sorted_squares_1([5])
