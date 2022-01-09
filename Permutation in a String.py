#  Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of s2.
#
#
#
# Example 1:
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true

import collections


def checkInclusion(self, s1: str, s2: str) -> bool:
    s1_c = collections.Counter(s1)
    i, j = 0, len(s1) - 1
    while j < len(s2):
        s2_c = collections.Counter(s2[i:j + 1])
        if s1_c == s2_c:
            return True
        j += 1
        i += 1
    return False