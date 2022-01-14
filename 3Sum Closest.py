#  Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
#
# Return the sum of the three integers.
#
# You may assume that each input would have exactly one solution.
#
#
#
# Example 1:
#
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

def threeSumClosest(self, nums: List[int], target: int) -> int:
    if not nums:
        return None
    nums.sort()
    res = sum(nums[::3])

    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while (l < r):
            cursum = nums[i] + nums[l] + nums[r]
            if abs(cursum - target) <= abs(res - target):
                res = cursum
            if cursum < target:
                l += 1
            elif cursum > target:
                r -= 1
            elif cursum == target:
                return cursum
    return res
