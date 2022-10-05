"""
Given an array of integers nums, sort it in ascending order using the quicksort algorithm.
"""

def quick_sort(nums, low=None, high=None, context=''):
    low = 0 if low is None else low
    high = len(nums) - 1 if high is None else high
    nums_len = high - low + 1
    print('{0}nums: {1}, length: {2}'.format(context, nums[low:high+1], nums_len))
    print('{0}low: {1}, high: {2}'.format(context, low, high))

    if nums_len < 2:
        print('{0}nums is already sorted'.format(context))
        return

    pivot = high
    i = low - 1
    for j in range(low, high):
        if nums[j] < nums[pivot]:
            i += 1
            print('{0}swapping {1} with {2}'.format(context, nums[i], nums[j]))
            nums[i], nums[j] = nums[j], nums[i]

    print('{0}swapping {1} with {2}'.format(context, nums[i + 1], nums[pivot]))
    nums[i + 1], nums[pivot] = nums[pivot], nums[i + 1]
    print('{0}sorted: {1}'.format(context, nums[low:high+1]))

    quick_sort(nums, low, i, context + ' ')
    quick_sort(nums, i + 2, high, context + ' ')

    print('{0}result: {1}'.format(context, nums))

if __name__ == '__main__':
    quick_sort([55, 23, 26, 2, 25])
