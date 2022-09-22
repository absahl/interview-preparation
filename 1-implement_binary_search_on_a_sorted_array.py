"""
We are given an array of integers, nums, sorted in ascending order, and an
integer value, target. If the target exists in the array, return its index.
If the target does not exist, then return -1.

The binary search divides the input array by half at every step.
After every step, either we find the index we are looking for, or we discard half of the array.
"""

def binary_search_iterative(nums, target):
    target_index = -1
    print('nums: {0}, target: {1}'.format(nums, target))

    nums_length = len(nums)
    if nums_length < 1:
        print(' invalid nums length: {0} - return {1}'.format(nums_length, target_index))
        return target_index

    if target == nums[nums_length - 1]:
        target_index = nums_length - 1
        print(' last index is the target - return {0}'.format(target_index))
        return target_index

    starting_index = 0
    last_index = nums_length - 1
    mid_index = int((starting_index + last_index) / 2)
    while True:
        print(' mid_index: {0}'.format(mid_index))

        if target == nums[mid_index]:
            print(' target found at index: {0}'.format(mid_index))
            target_index = mid_index
            break

        if target < nums[mid_index]:
            print(' target is smaller than mid_index, moving to left sub array')
            last_index = mid_index
        else:
            print(' target is larger than mid_index, moving to right sub array')
            starting_index = mid_index

        new_mid_index = int((starting_index + last_index) / 2)
        if new_mid_index == mid_index:
            print(' new_mid_index is same as mid_index')
            break
            
        mid_index = new_mid_index

    print(' return {0}'.format(target_index))
    return target_index

def binary_search_iterative_1(nums, target):
    target_index = -1
    print('nums: {0}, target: {1}'.format(nums, target))

    starting_index = 0
    last_index = len(nums) - 1
    while starting_index <= last_index and target_index == -1:
        mid_index = (starting_index + last_index) // 2
        print(' mid_index: {0}'.format(mid_index))

        if target == nums[mid_index]:
            print(' target found at index: {0}'.format(mid_index))
            target_index = mid_index
        elif target < nums[mid_index]:
            print(' target is smaller than mid_index, moving to left sub array')
            last_index = mid_index - 1
        else:
            print(' target is larger than mid_index, moving to right sub array')
            starting_index = mid_index + 1

    print(' return {0}'.format(target_index))
    return target_index

def binary_search_recursive(nums, target):
    if not nums:
        return -1

    mid_index = (len(nums) - 1) // 2
    if target == nums[mid_index]:
        return mid_index
    elif target < nums[mid_index]:
        return binary_search_recursive(nums[0:mid_index], target)
    else:
        relative_index = binary_search_recursive(nums[mid_index + 1:], target)
        return -1 if relative_index == -1 else relative_index + mid_index + 1

if __name__ == '__main__':
    """binary_search_iterative_1([], 12)
    binary_search_iterative_1([0,1], 1)
    binary_search_iterative_1([1,2,3], 3)
    binary_search_iterative_1([-1,0,3,5,9,12], 9)
    binary_search_iterative_1([-1,0,3,5,9,12], 2)"""

    print(f'nums: [], target: 12, result: {binary_search_recursive([], 12)}')
    print(f'nums: [0,1], target: 1, result: {binary_search_recursive([0,1], 1)}')
    print(f'nums: [1,2,3], target: 3, result: {binary_search_recursive([1,2,3], 3)}')
    print(f'nums: [-1,0,3,5,9,12], target: 9, result: {binary_search_recursive([-1,0,3,5,9,12], 9)}')
    print(f'nums: [-1,0,3,5,9,12], target: 2, result: {binary_search_recursive([-1,0,3,5,9,12], 2)}')
