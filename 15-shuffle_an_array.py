"""
Shuffle an array randomly with all permutations as equally likely.

Given an integer array nums, write an algorithm to shuffle the array randomly.
All permutations of the array should be equally likely.

Implement three functions of the Solution class:

Initializes the object with the integer array nums.
Resets the array to its original configuration and returns it.
Returns a random shuffling of the array.

Example#
Sample input#
[2, 4, 5]
Expected output#
Permutation  |  Occurrences | Frequency
[2, 4, 5]    |    150 times | 16.67%
[2, 5, 4]    |    150 times | 16.67%
[4, 2, 5]    |    150 times | 16.67%
[4, 5, 2]    |    150 times | 16.67%
[5, 2, 4]    |    150 times | 16.67%
[5, 4, 2]    |    150 times | 16.67%

Ideally, each permutation of the array should have an equal chance of appearing.
With an input array of 3 elements, the number of possible permutations of size 3 is 6.
Thus, we expect each permutation to show up with a probability of 1/6.
When we shuffle the given array 900 times, we want each permutation to appear approximately 150 times.
"""

import random
import math

class Solution:
    original = None
    n = None

    def __init__(self, nums):
        self.nums = nums
        self.total_permutations = math.factorial(len(nums))
        print('nums: {0}, total permutations: {1}'.format(self.nums, self.total_permutations))

    def reset(self):
        return self.nums

    def shuffle(self):
        temp = list(self.nums)
        remaining_permutations = self.total_permutations
        shuffler = random.randrange(0, self.total_permutations)

        shuffled = list(self.nums)
        for i in range(len(self.nums) - 1, -1, -1):
            divider = remaining_permutations // (i + 1)
            ith_index = shuffler // divider
            print(' i: {0}, ith_index: {1}, remaining permutations: {2}, divider: {3}, shuffler: {4}'.format(i, ith_index, remaining_permutations, divider, shuffler))
            shuffled[i] = temp.pop(ith_index)
            remaining_permutations = divider
            shuffler %= divider

        print(' shuffled: {0}'.format(shuffled))
        return shuffled

class Solution2:
    """
    Init: Set nums and its length
    Reset: No need to reset. Just return the original.
    Shuffle: For array with length n, generate random number n - 1 times to
    populate the unshuffled part of array.
    """

    def __init__(self, nums):
        self.original = nums
        print('original: {0}, n: {1}'.format(self.original, len(self.original)))

    def reset(self):
        return self.original

    def shuffle(self):
        shuffled = list(self.original)
        for i in range(len(self.original) - 1, 0, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

        print(' shuffled: {0}'.format(shuffled))
        return shuffled

if __name__ == '__main__':
    solution = Solution2([2, 4, 5])
    solution.shuffle()
