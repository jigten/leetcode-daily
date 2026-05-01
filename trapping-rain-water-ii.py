"""
407. Trapping Rain Water II
Hard

Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:
Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.

Example 2:
Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10

Constraints:
* m == heightMap.length
* n == heightMap[i].length
* 1 <= m, n <= 200
* 0 <= heightMap[i][j] <= 2 * 10^4
"""

import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        rows, cols = len(heightMap), len(heightMap[0])
        pq = []

        for r in range(rows):
            pq.append((heightMap[r][0], r, 0))
            pq.append((heightMap[r][cols - 1], r, cols - 1))
        
        for c in range(cols):
            pq.append((heightMap[0][c], 0, c))
            pq.append((heightMap[rows - 1][c], rows - 1, c))
        
        seen = set([(r, c) for _, r, c in pq])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0
        heapq.heapify(pq)

        while pq:
            h, r, c = heapq.heappop(pq)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                    if heightMap[nr][nc] <= h:
                        res += h - heightMap[nr][nc]
                        
                    seen.add((nr, nc))
                    heapq.heappush(pq, (max(heightMap[nr][nc], h), nr, nc))
        return res

def test_trapping_rain_water_ii():
    solution = Solution()
    
    # Test case 1
    heightMap1 = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    expected1 = 4
    result1 = solution.trapRainWater(heightMap1)
    assert result1 == expected1, f"Test case 1 failed: expected {expected1}, got {result1}"
    
    # Test case 2
    heightMap2 = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    expected2 = 10
    result2 = solution.trapRainWater(heightMap2)
    assert result2 == expected2, f"Test case 2 failed: expected {expected2}, got {result2}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_trapping_rain_water_ii()


