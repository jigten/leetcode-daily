from typing import List


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        s_arr, d_arr = [], []
        max_s, max_d = (float("-inf"), -1), (float("-inf"), -1)
        min_s, min_d = (float("inf"), -1), (float("inf"), -1)

        for i, (x, y) in enumerate(points):
            s, d = x + y, x - y
            s_arr.append(s)
            d_arr.append(d)

            if s < min_s[0]:
                min_s = (s, i)

            if s > max_s[0]:
                max_s = (s, i)

            if d < min_d[0]:
                min_d = (d, i)

            if d > max_d[0]:
                max_d = (d, i)

        res = float("inf")
        for v, idx in [min_s, max_s, min_d, max_d]:
            c_max_s, c_min_s = float("-inf"), float("inf")
            c_max_d, c_min_d = float("-inf"), float("inf")

            for i, (s, d) in enumerate(zip(s_arr, d_arr)):
                if i == idx:
                    continue

                c_max_s = max(c_max_s, s)
                c_min_s = min(c_min_s, s)
                c_max_d = max(c_max_d, d)
                c_min_d = min(c_min_d, d)

            res = min(res, max(c_max_s - c_min_s, c_max_d - c_min_d))

        return res
