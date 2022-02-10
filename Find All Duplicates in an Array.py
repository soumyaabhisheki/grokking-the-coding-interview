#  Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
#
# You must write an algorithm that runs in O(n) time and uses only constant extra space.
#
#
#
# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

def findDuplicates(self, nums):
    res = []
    for n in nums:
        n = abs(n)
        if nums[n - 1] > 0:
            nums[n - 1] *= -1
        else:
            res.append(n)
    return res
