from typing import List


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rotatedBox = [['.'] * len(boxGrid) for _ in range(len(boxGrid[0]))]
        rows, cols = len(rotatedBox), len(rotatedBox[0])

        for r in range(rows):
            for c in range(cols):
                rotatedBox[r][c] = boxGrid[len(boxGrid) - 1 - c][r]

        for c in range(cols):
            empty_slot = rows - 1

            for curr in range(rows - 1, -1, -1):
                cell = rotatedBox[curr][c]
                if cell == '*':
                    empty_slot = curr - 1
                elif cell == '#':
                    if curr < empty_slot:
                        rotatedBox[empty_slot][c] = '#'
                        rotatedBox[curr][c] = '.'

                    empty_slot -= 1

        return rotatedBox


solution = Solution()
assert solution.rotateTheBox(boxGrid=[["#", ".", "#"]]) == [["."], ["#"], ["#"]]
assert solution.rotateTheBox([["#", ".", "*", "."], ["#", "#", "*", "."]]) == [
    ["#", "."],
    ["#", "#"],
    ["*", "*"],
    [".", "."],
]
