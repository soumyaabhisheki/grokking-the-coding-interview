#  Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
#
#
#
# Example 1:
#
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
import math


def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    i, j = 0, 0
    res = math.inf
    summation = 0
    while j < len(nums):
        summation = summation + nums[j]
        if summation < target:
            j += 1
        else:
            while summation >= target:
                res = min(res, j - i + 1)
                summation = summation - nums[i]
                i += 1
            j += 1
    if res is math.inf:
        return 0
    else:
        return res