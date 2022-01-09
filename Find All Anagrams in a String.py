#  Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
#
#
# Example 1:
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]

import collections


def findAnagrams(self, s: str, p: str):
    myDictP = collections.Counter(p)
    myDictS = collections.Counter(s[:len(p)])
    output = []
    i = 0
    j = len(p)
    while (j <= len(s)):
        if myDictS == myDictP:
            output.append(i)
        myDictS[s[i]] -= 1
        if myDictS[s[i]] <= 0:
            myDictS.pop(s[i])

        if j < len(s):
            myDictS[s[j]] += 1
        j += 1
        i += 1
    return output