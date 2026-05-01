from typing import List
import heapq

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        seen = set()
        pq = []

        def getRhombusSums(r, c, pq):
            limit = min(r, c, rows - r - 1, cols - c - 1)

            if grid[r][c] not in seen:
                seen.add(grid[r][c])
                heapq.heappush(pq, -grid[r][c])
            
            for k in range(1, limit + 1):
                edges = [
                    [(r, c - k), (-1 ,1)], # left to top
                    [(r - k, c), (1, 1)], # top to right
                    [(r, c + k), (1, -1)], # right to bottom
                    [(r + k, c), (-1, -1)] # bottom to left
                ]

                curr_sum = 0

                for (cr, cc), (dr, dc) in edges:
                    for i in range(k):
                        curr_sum += grid[cr + i*dr][cc + i*dc]
                
                if curr_sum not in seen:
                    seen.add(curr_sum)
                    heapq.heappush(pq, -curr_sum)
 

        for r in range(rows):
            for c in range(cols):
                getRhombusSums(r, c, pq)
        
        res = []
        while pq and len(res) < 3:
            res.append(-heapq.heappop(pq))
        
        return res
