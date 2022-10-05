"""
We're given an integer array, nums.
Move all zeroes if any to the left while maintaining the order of other elements in the array.
"""

def move_zeros_to_left(nums):
    print('input: {0}'.format(nums))

    temp = [0] * len(nums)
    j = len(nums) - 1
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] != 0:
            temp[j] = nums[i]
            j -= 1

    nums = temp
    print(' output: {0}'.format(nums))

def move_zeros_to_left_1(nums):
    print('input: {0}'.format(nums))

    rp = wp = len(nums) - 1
    while rp >= 0:
        if nums[rp] != 0:
            nums[wp] = nums[rp]
            wp -= 1

        rp -= 1

    for i in range(0, wp + 1):
        nums[i] = 0

    print(' output: {0}'.format(nums))

if __name__ == '__main__':
    move_zeros_to_left_1([1, 10, 20, 0, 59, 63, 0, 88, 0])
    move_zeros_to_left_1([1, 10, 20, 0, 59, 63, 0, 88, 0])
    move_zeros_to_left([1, 0, 2, 3, 0])
    move_zeros_to_left([0])
    move_zeros_to_left([-1, 0, 0, -2, 9])
    move_zeros_to_left([1, 2, 3, 4, 5])
    move_zeros_to_left([2])
