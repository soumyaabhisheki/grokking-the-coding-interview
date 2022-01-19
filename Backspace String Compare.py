#  Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
#
#
# Example 1:
#
# Input: s = "ab#c", t = "ad#c"
# Output: true

def backspaceCompare(self, S: str, T: str) -> bool:
    def it(s):
        cnt = 0
        for ch in reversed(s):
            if ch != '#' and cnt == 0:
                yield
            else:
                if ch == '#':
                    cnt += 1
                else:
                    cnt -= 1

        yield ''  # indicate the end of iterator

    return all(s == t for s, t in zip(it(S), it(T)))