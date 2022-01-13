#  Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
#
#
#
# Example 1:
#
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

def numSubarrayProductLessThanK(self, nums):
    i, j, output = 0, 0, 0
    product = 1
    while j < len(nums):
        product = product * nums[j]
        while (product >= k) and i <= j:
            product = product / nums[i]
            i += 1
        output += j - i + 1
        j += 1
    return output