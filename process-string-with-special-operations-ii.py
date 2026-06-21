class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = 0

        for c in s:
            if c == '*':
                n = max(0, n - 1)
            elif c == '#':
                n *= 2
            elif c == '%':
                pass
            else:
                n += 1

        if n <= k: return '.'

        for i in range(len(s) - 1, -1, -1):
            c = s[i]

            if c == '*':
                n += 1
            elif c == '#':
                n = n // 2
                if k >= n:
                    k -= n
            elif c == '%':
                k = n - k - 1
            else:
                n -= 1
                if k == n:
                    return c

        return '.'
