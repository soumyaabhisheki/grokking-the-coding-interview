#  Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
#
#
#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]

def sortedSquares(self, nums):
    l, r = 0, len(nums) - 1
    res = []
    while l <= r:
        if abs(nums[l]) >= abs(nums[r]):
            res.append(nums[l] * nums[l])
            l += 1
        else:
            res.append(nums[r] * nums[r])
            r -= 1
    return res[::-1]  # reverse