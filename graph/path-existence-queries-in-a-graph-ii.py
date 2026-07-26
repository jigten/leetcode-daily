from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:
        sorted_pos = list(sorted((n, i) for i, n in enumerate(nums)))
        pos_to_sorted_pos = [-1] * n

        # map from original idx to where in the sorted array idx
        for sorted_idx in range(n):
            pos_to_sorted_pos[sorted_pos[sorted_idx][1]] = sorted_idx

        counter = 0
        comps = [-1] * n
        comps[sorted_pos[0][1]] = counter

        for i in range(1, n):
            if sorted_pos[i][0] - sorted_pos[i - 1][0] > maxDiff:
                counter += 1

            comps[sorted_pos[i][1]] = counter

        # furthest right we can jump from each index based on maxDiff limit
        next_right = [-1] * n
        j = 0

        for i in range(n):
            while j + 1 < n and sorted_pos[j + 1][0] - sorted_pos[i][0] <= maxDiff:
                j += 1
            next_right[i] = j

        LOG = 18
        up = [[0] * LOG for _ in range(n)]
        for i in range(n):
            up[i][0] = next_right[i]

        for j in range(1, LOG):
            for i in range(n):
                mid_jump = up[i][j - 1]
                final_dest = up[mid_jump][j - 1]
                up[i][j] = final_dest

        res = [0] * len(queries)
        for i, (qa, qb) in enumerate(queries):
            if qa == qb:
                res[i] = 0
                continue

            if comps[qa] != comps[qb]:
                res[i] = -1
                continue

            curr, target = pos_to_sorted_pos[qa], pos_to_sorted_pos[qb]
            if curr > target:
                curr, target = target, curr

            steps = 0
            for k in range(LOG - 1, -1, -1):
                if up[curr][k] < target:
                    curr = up[curr][k]
                    steps += 1 << k

            res[i] = steps + 1

        return res
