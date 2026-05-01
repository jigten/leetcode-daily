from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        curr_d = 0 
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        x, y = 0, 0
        obs = {tuple(o) for o in obstacles}

        res = 0
        for command in commands:
            if command == -1:
                curr_d = (curr_d + 1) % 4 
            elif command == -2:
                curr_d = (curr_d - 1) % 4
            else:
                dx, dy = directions[curr_d]
                for _ in range(command):
                    if (x + dx, y + dy) in obs:
                        break 
                    
                    x += dx
                    y += dy
                
                res = max(res, x * x + y * y)

        return res
        
solution = Solution()
print(solution.robotSim(commands = [4,-1,3], obstacles = []))
print(solution.robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]]))
print(solution.robotSim(commands = [6,-1,-1,6], obstacles = [[0,0]]))
