from typing import List

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        ports = {
            1: {'L', 'R'},
            2: {'U', 'D'},
            3: {'L', 'D'},
            4: {'R', 'D'},
            5: {'L', 'U'},
            6: {'R', 'U'}
        }

        moves = {
            'U': (-1, 0, 'D'),
            'D': (1, 0, 'U'),
            'L': (0, -1, 'R'),
            'R': (0, 1, 'L')
        }

        seen = set()
        def dfs(r, c):
            if (r, c) == (rows - 1, cols - 1):
                return True
            
            if (r, c) in seen:
                return False
            
            seen.add((r, c))

            curr = grid[r][c]
            curr_ports = ports[curr]

            for port in curr_ports:
                dr, dc, np = moves[port]
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    next_pos = grid[nr][nc]
                    if np in ports[next_pos]:
                        if dfs(nr, nc):
                            return True

            return False

        return dfs(0, 0)

solution = Solution()
assert(solution.hasValidPath(grid = [[2,4,3],[6,5,2]]) == True)
assert(solution.hasValidPath(grid = [[1,2,1],[1,2,1]]) == False)
assert(solution.hasValidPath(grid = [[1,1,2]]) == False)