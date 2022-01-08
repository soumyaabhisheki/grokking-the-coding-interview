# Problem Statement
# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.
# Example 1:
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:
# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9

def longest_ones(self, nums: List[int], k: int) -> int:
    n, ans, l = len(nums), 0, 0
    for r in range(n):
        if nums[r] == 0:  # try to pick current 0
            if k == 0:  # if window already picked k zeros, pop 1 from left and pick this
                while nums[l] != 0: l += 1
                l += 1
            else:
                k -= 1  # otherwise pick it and decrement k
        ans = max(ans, r - l + 1)  # update ans as max window size till now
    return ans
