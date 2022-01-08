# Problem Statement
# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.
# Example 1:
# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:
# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:
# Input: String="abccde", k=1
# Output: 3

def character_replacement(self, s: str, k: int) -> int:
    l, r, res, maxf = 0, 0, 0, 0
    count = {}
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while ((r - l + 1) - maxf) > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, (r - l + 1))
    return res
