# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum.
# A sub array is a contiguous part of an array.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:
# Input: nums = [1]
# Output: 1

def maxSubArray(self, nums):
    curSum = maxSum = nums[0]
    for num in nums[1:]:
        curSum = max(curSum + num, num)
        maxSum = max(maxSum, curSum)
    return maxSum
