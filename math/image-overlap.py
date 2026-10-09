from collections import defaultdict
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        b = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        cnts = defaultdict(int)
        res = 0

        for ar, ac in a:
            for br, bc in b:
                dx, dy = br - ar, bc - ac
                cnts[(dx, dy)] += 1
                res = max(res, cnts[(dx, dy)])

        return res
