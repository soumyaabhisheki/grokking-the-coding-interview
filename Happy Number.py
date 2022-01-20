#  Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.
#
#
#
# Example 1:
#
# Input: n = 19
# Output: true
#  Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
# Example 2:
#
# Input: n = 2
# Output: false

def isHappy(self, n: int) -> bool:
    # 20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
    slow = self.squared(n)
    fast = self.squared(self.squared(n))

    while slow != fast and fast != 1:
        slow = self.squared(slow)
        fast = self.squared(self.squared(fast))

    return fast == 1


def squared(self, n):
    result = 0
    while n > 0:
        last = n % 10
        result += last * last
        n = n // 10
    return result