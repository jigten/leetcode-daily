from bisect import bisect_right
from typing import List


class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        n = len(tasks)
        res = []
        pref = [0] * (n + 1)

        for i in range(1, n + 1):
            pref[i] = tasks[i - 1] + pref[i - 1]

        i, rem = 0, tasks[0]
        T = pref[n]

        for b in shifts:
            start = pref[i] + (tasks[i] - rem)

            if start + b >= T:
                res.append(0)
                i, rem = 0, tasks[0]
            else:
                W = start + b
                i = bisect_right(pref, W) - 1
                rem = pref[i + 1] - W
                res.append(n - i)

        return res
