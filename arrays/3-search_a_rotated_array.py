"""
We're given a sorted integer array, nums and an integer value, target.
The array is rotated by some arbitrary number. Search the target in this array.
If the target does not exist then return -1.
"""

def binary_search_rotated(nums, target):
    print('nums ({0}): {1}, target: {2}'.format(len(nums), nums, target))

    context = ' '
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        print('{0}nums ({1}): {2}, low: {3}, mid = {4}, high: {5}'.format(context, high + 1 - low, nums[low : high + 1], low, mid, high))
        context = ' {0}'.format(context)

        if target == nums[mid]:
            print('{0}target found at index {1}'.format(context, mid))
            return mid
        elif target < nums[mid]:
            print('{0}target is smaller than mid'.format(context))
            if nums[low] < nums[mid]:
                print('{0}left sub array is ordered'.format(context))
                if target >= nums[low]:
                    print('{0}target is greater than low - moving to left subtree'.format(context))
                    high = mid - 1
                else:
                    print('{0}target is smaller than low - moving to right subtree'.format(context))
                    low = mid + 1
            else:
                print('{0}right sub array is ordered'.format(context))
                high = mid - 1
        else:
            print('{0}target is greater than mid'.format(context))
            if nums[mid] < nums[high]:
                print('{0}right sub array is ordered'.format(context))
                if target <= nums[high]:
                    print('{0}target is smaller than high - moving to right subtree'.format(context))
                    low = mid + 1
                else:
                    print('{0}target is greater than high - moving to left subtree'.format(context))
                    high = mid - 1
            else:
                print('{0}right sub array is ordered'.format(context))
                low = mid + 1

    return -1

def binary_search_rotated_1(nums, target):
    result = -1

    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == nums[mid]:
            result = mid
            break

        if nums[low] < nums[mid]:
            if target < nums[mid] and target >= nums[low]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if target > nums[mid] and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    print('nums: {0}, target: {1}, result: {2}'.format(nums, target, result))
    return result

if __name__ == '__main__':
    binary_search_rotated_1([6, 7, 1, 2, 3, 4, 5],3)
    binary_search_rotated_1([6, 7, 1, 2, 3, 4, 5],6)
    binary_search_rotated_1([4, 5, 6, 1, 2, 3],3)
    binary_search_rotated_1([4, 5, 6, 1, 2, 3],6)
    binary_search_rotated_1([4],1)
