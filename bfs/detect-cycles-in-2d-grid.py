from typing import List
from collections import deque

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        seen = set()
        for r in range(rows):
            for c in range(cols):
                if (r, c) in seen: continue
            
                q = deque([(-1, -1, r, c)])

                while q:
                    prev_r, prev_c, r, c = q.popleft()

                    seen.add((r, c))
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[r][c] == grid[nr][nc]:
                            if (nr, nc) == (prev_r, prev_c): continue

                            if (nr, nc) in seen: return True

                            seen.add((nr, nc))
                            q.append((r, c, nr, nc))
                
        return False

        def dfs(prev_r, prev_c, r, c, path_len):
            seen.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[r][c] == grid[nr][nc]:
                    if (nr, nc) == (prev_r, prev_c): continue

                    if (nr, nc) in seen: return path_len >= 4 

                    if dfs(r, c, nr, nc, path_len + 1): return True
            
            return False
                

        for r in range(rows):
            for c in range(cols):
                if dfs(-1, -1, r, c, 1): return True

        return False

solution = Solution()
assert(solution.containsCycle(grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]) == True)
assert(solution.containsCycle(grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]) == True)
assert(solution.containsCycle(grid = [["a","b","b"],["b","z","b"],["b","b","a"]]) == False)