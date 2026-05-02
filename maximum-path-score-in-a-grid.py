from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        NEG = -(10**9)
        prev_row = [[NEG] * (k + 1) for _ in range(cols)]

        for r in range(rows):
            curr_row = [[NEG] * (k + 1) for _ in range(cols)]

            for c in range(cols):
                score = grid[r][c]
                cost = 1 if score > 0 else 0

                if r == 0 and c == 0:
                    if cost <= k:
                        curr_row[0][cost] = score
                    continue

                for curr_cost in range(cost, k + 1):
                    best = NEG
                    if r > 0 and prev_row[c][curr_cost - cost] != NEG:
                        best = max(
                            best,
                            prev_row[c][curr_cost - cost] + score,
                        )

                    if c > 0 and curr_row[c - 1][curr_cost - cost] != NEG:
                        best = max(
                            best,
                            curr_row[c - 1][curr_cost - cost] + score,
                        )

                    curr_row[c][curr_cost] = best

            prev_row = curr_row

        ans = max(prev_row[cols - 1])
        return -1 if ans == NEG else ans


solution = Solution()
assert solution.maxPathScore(grid=[[0, 1], [2, 0]], k=1) == 2
assert solution.maxPathScore(grid=[[0, 1], [1, 2]], k=1) == -1
