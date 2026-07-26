from collections import deque


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        theifs = [[float("inf")] * cols for _ in range(rows)]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    theifs[r][c] = 0
                    q.append((r, c, 0))

        while q:
            cr, cc, d = q.popleft()

            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if 0 <= nr < rows and 0 <= nc < cols and theifs[nr][nc] > (d + 1):
                    theifs[nr][nc] = d + 1
                    q.append((nr, nc, d + 1))

        def isValid(m):
            if theifs[0][0] < m:
                return False
            stack = [(0, 0)]
            seen = set([(0, 0)])

            while stack:
                r, c = stack.pop()

                if r == rows - 1 and c == cols - 1:
                    return True

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and (nr, nc) not in seen
                        and theifs[nr][nc] >= m
                    ):
                        seen.add((nr, nc))
                        stack.append((nr, nc))

            return False

        print(theifs)
        l, r, res = 0, 0, -1

        for row in theifs:
            for v in row:
                r = max(r, v)

        while l <= r:
            m = l + (r - l) // 2
            if isValid(m):
                res = m
                l = m + 1
            else:
                r = m - 1

        return res
