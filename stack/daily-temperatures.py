from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, prev_id = stack.pop()
                res[prev_id] = i - prev_id

            stack.append((t, i))

        return res
