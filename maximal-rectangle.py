from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols

        for c in range(cols):
            heights[c] = int(matrix[0][c])

        def findMaxRect(heights):
            stack = []
            max_ht = 0

            for i, h in enumerate(heights + [0]):
                while stack and stack[-1][0] > h:
                    prev_h, _ = stack.pop()
                    width = i if not stack else (i - stack[-1][1] - 1)
                    max_ht = max(max_ht, prev_h * width)

                stack.append((h, i))

            return max_ht

        res = findMaxRect(heights)
        for r in range(1, rows):
            for c in range(cols):
                heights[c] = heights[c] + 1 if matrix[r][c] == "1" else 0

            res = max(res, findMaxRect(heights))

        return res
