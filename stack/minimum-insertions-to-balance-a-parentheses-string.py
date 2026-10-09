class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        stack = []
        i, n = 0, len(s)

        while i < n:
            if s[i] == "(":
                stack.append(s[i])
                i += 1
            else:
                if i + 1 < n and s[i + 1] == ")":
                    if not stack:
                        res += 1
                    else:
                        stack.pop()

                else:
                    res += 1
                    if stack:
                        stack.pop()
                    else:
                        res += 1

        return res + 2 * len(stack)
