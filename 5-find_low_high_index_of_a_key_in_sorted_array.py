"""
We're given a sorted array of integers, nums, and an integer value, target.
Return the low and high index of the given target element.
If the indexes are not found, return -1.

Note: The array can contain multiple duplicates with length in millions.
"""

def find_low_index(nums, target):
    low = 0
    high = len(nums) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2

        if target == nums[mid]:
            if mid == 0 or nums[mid] != nums[mid - 1]:
                result = mid
                break
            else:
                high = mid - 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    print('nums: {0}, target: {1}, result: {2}'.format(nums, target, result))
    return result

def find_high_index(nums, target):
    low = 0
    high = len(nums) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2

        if target == nums[mid]:
            if mid == len(nums) - 1 or nums[mid] != nums[mid + 1]:
                result = mid
                break
            else:
                low = mid + 1
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1

    print('nums: {0}, target: {1}, result: {2}'.format(nums, target, result))
    return result

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    target = 5
    find_low_index(nums, target)
    find_high_index(nums, target)
