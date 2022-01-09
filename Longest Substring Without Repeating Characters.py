#  Given a string s, find the length of the longest substring without repeating characters.
#
#
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def lengthOfLongestSubstring(self, s: str) -> int:
    i, j, maxlen = 0, 0, 0
    my_set = set()
    while j < len(s):
        if s[j] not in my_set:
            my_set.add(s[j])
            j += 1
        else:
            while s[j] in my_set:
                my_set.remove(s[i])
                i += 1
        maxlen = max(maxlen, len(my_set))
    return maxlen
