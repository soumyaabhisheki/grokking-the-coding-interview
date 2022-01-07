# Problem Statement Given an array of characters where each character represents a fruit tree, you are given two
# baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket
# can have only one type of fruit. You can start with any tree, but once you have started you can’t skip a tree. You
# will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit
# type. Write a function to return the maximum number of fruits in both the baskets.
# Example 1: Input: Fruit=['A', # 'B', 'C', 'A', 'C']
# Output: 3 Explanation: We can put 2 'C' in one basket and one 'A' in the other from the
# subarray ['C', 'A', 'C'] Example 2: Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C'] Output: 5 Explanation: We can put 3
# 'B' in one basket and two 'C' in the other basket. This can be done if we start with the second letter: ['B', 'C',
# 'B', 'B', 'C']
from typing import List


class Solution:
    def total_fruit(self, fruits: List[int]) -> int:
        i, j = 0, 0
        maximum = 0
        basket = {}

        while j < len(fruits):

            if fruits[j] in basket:
                basket[fruits[j]] += 1
                j = j + 1

            else:
                basket[fruits[j]] = 1
                j = j + 1
                while len(basket) > 2:
                    basket[fruits[i]] -= 1
                    if basket[fruits[i]] == 0:
                        del basket[fruits[i]]
                    i = i + 1
            maximum = max(maximum, sum(basket.values()))
        return maximum
