from typing import List

class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = sorted(zip(range(len(positions)), positions, healths, directions), key=lambda x: x[1])
        stack = []
        res = []

        for idx, pos, health, direction in robots:
            if direction == 'R':
                stack.append((idx, pos, health, direction))
            else:
                while stack and health > 0:
                    prev_robot_idx, prev_robot_pos, prev_robot_health, prev_robot_dir = stack.pop()

                    if prev_robot_health > health:
                        health = 0
                        prev_robot_health -= 1
                        stack.append((prev_robot_idx, prev_robot_pos, prev_robot_health, prev_robot_dir))
                        break
                    elif prev_robot_health == health:
                        health = 0
                        break
                    else:
                        health -= 1

                if health > 0:
                    res.append((idx, pos, health, direction))

        for survivor in stack:
            res.append(survivor)
        
        res.sort(key=lambda x: x[0])

        return [h for i, p, h, d in sorted(res)]

        
solution = Solution()

print(solution.survivedRobotsHealths(positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"))