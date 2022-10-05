"""
We're given an array of integers, nums. Rotate the array by n elements, where n is an integer:

For positive values of n, perform a right rotation.
For negative values of n, perform a left rotation.
Make sure we make changes to the original array.
"""

def rotate_array(nums, n):
    print('nums: {0}, n: {1}'.format(nums, n))

    nums_length = len(nums)
    if nums_length < 2:
        print(' array size is: {0} - no need for rotation'.format(nums_length))
        return

    rotations = (nums_length + n) % nums_length
    print(' right rotations required: {0}'.format(rotations))
    if rotations == 0:
        return

    # take backup of last n elements
    temp_nums = nums[-n:]

    # shift first total - n elements to right
    nums[n:] = nums[:-n]

    # restore backup elements to left most of the list
    nums[:n] = temp_nums

    print(' result: {0}'.format(nums))

def reverse_array(nums, low, high):
    high = high if high < len(nums) else len(nums) - 1

    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low += 1
        high -= 1

def rotate_array_1(nums, n):
    print('nums: {0}, n: {1}'.format(nums, n))

    nums_length = len(nums)
    if nums_length < 2:
        print(' array size is: {0} - no need for rotation'.format(nums_length))
        return

    n = (nums_length + n) % nums_length
    #print(' right rotations required: {0}'.format(n))
    if n == 0:
        return

    reverse_array(nums, 0, nums_length - 1)
    #print(' array reversed: {0}'.format(nums))
    reverse_array(nums, 0, n - 1)
    #print(' left sub array reversed: {0}'.format(nums))
    reverse_array(nums, n, nums_length - 1)

    print(' result: {0}'.format(nums))

if __name__ == '__main__':
    rotate_array_1([-1, -100, 3, 99], 2)
    rotate_array_1([1, 2, 3, 4, 5], 2)
    rotate_array_1([1, 2, 3, 4, 5, 6, 7], 3)
    rotate_array_1([1, 10, 20, 0, 59, 86, 32, 11, 9, 40], -3)
    rotate_array_1([1, 2], 1)
