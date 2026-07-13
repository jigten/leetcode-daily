from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        def dfs(curr, last_digit):
            if low <= curr <= high:
                res.append(curr)

            if curr > high:
                return

            if last_digit == 9:
                return

            dfs(curr * 10 + (last_digit + 1), last_digit + 1)

        for i in range(1, 10):
            dfs(i, i)

        res.sort()
        return res
