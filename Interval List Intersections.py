#  Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
# Example 1:
# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.
# Example 2:
# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.

def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    i = 0
    j = 0

    result = []
    while i < len(A) and j < len(B):
        a_start, a_end = A[i]
        b_start, b_end = B[j]
        if a_start <= b_end and b_start <= a_end:  # Criss-cross lock
            result.append([max(a_start, b_start), min(a_end, b_end)])  # Squeezing

        if a_end <= b_end:  # Exhausted this range in A
            i += 1  # Point to next range in A
        else:  # Exhausted this range in B
            j += 1  # Point to next range in B
    return result
