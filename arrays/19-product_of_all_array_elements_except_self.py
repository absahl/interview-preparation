"""
Calculate the product of all the elements of an array except the current
element.

Given an integer array, nums, return an array, answer, such that answer[i] is
equal to the product of all the elements of nums except nums[i].

Sample input#
nums = [1, 2, 3, 4]
Expected output#
[24, 12, 8, 6]

Sample input#
nums = [-1, 1, 0, -3, 3]
Expected output#
[0, 0, 9, 0, 0]
"""

def product_except_self(nums):
    """
    Time complexity: O(N)
    Space complexity: O(1)
    """

    print('nums: {0}'.format(nums))
    nums_len = len(nums) # O(N)

    answer = [0] * nums_len
    zeros = nums.count(0) # O(N)
    if zeros > 1:
        pass
    elif zeros == 1:
        non_zero_product = 1
        zero_element_index = -1
        for i in range(nums_len): # O(N)
            if nums[i] == 0:
                zero_element_index = i
            else:
                non_zero_product *= nums[i]

        answer[zero_element_index] = non_zero_product
    else:
        total_product = 1
        for i in range(nums_len): # O(N)
            total_product *= nums[i]

        for i in range(nums_len): # O(N)
            answer[i] = total_product // nums[i]

    print(' answer: {0}'.format(answer))
    return answer

if __name__ == '__main__':
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert product_except_self([1, 2]) == [2, 1]
    assert product_except_self([2, 4, 6, 8]) == [192, 96, 64, 48]
    assert product_except_self([5, 10, 15, 20, 25, 30]) == [2250000, 1125000, 750000, 562500, 450000, 375000]
