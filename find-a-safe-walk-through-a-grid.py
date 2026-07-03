import heapq
from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        max_healths = [[-1] * cols for _ in range(rows)]

        if grid[0][0] >= health:
            return False

        start_health = health - grid[0][0]
        max_healths[0][0] = start_health

        # 01 DFS method
        q = deque([(0, 0, start_health)])

        while q:
            cr, cc, ch = q.popleft()

            if cr == rows - 1 and cc == cols - 1 and ch >= 1:
                return True

            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    next_h = ch - grid[nr][nc]

                    if next_h > max_healths[nr][nc]:
                        max_healths[nr][nc] = next_h

                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc, next_h))
                        else:
                            q.append((nr, nc, next_h))

        return False

        # Djikstra method
        max_healths = [[-1] * cols for _ in range(rows)]
        max_healths[0][0] = health - grid[0][0]
        pq = [(-(health - grid[0][0]), 0, 0)]

        while pq:
            ch, cr, cc = heapq.heappop(pq)
            ch = -ch

            if cr == rows - 1 and cc == cols - 1 and ch >= 1:
                return True

            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and max_healths[nr][nc] < ch - grid[nr][nc]
                ):
                    max_healths[nr][nc] = ch - grid[nr][nc]
                    heapq.heappush(pq, (-(ch - grid[nr][nc]), nr, nc))

        return False
