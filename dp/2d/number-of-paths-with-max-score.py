from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        rows, cols = len(board), len(board[0])
        # [score, path]
        dp = [[[0, 0] for _ in range(cols)] for _ in range(rows)]
        dp[rows - 1][cols - 1][1] = 1

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "X":
                    dp[r][c][0] = -1
                    dp[r][c][1] = 0

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if r == rows - 1 and c == cols - 1:
                    continue

                curr_score = 0
                if board[r][c] != "E" or board[r][c] != "X":
                    curr_score = int(board[r][c])

                if c < cols - 1 and dp[r][c + 1][1] > 0:
                    if curr_score + dp[r][c + 1][0] > dp[r][c][0]:
                        dp[r][c] = [curr_score + dp[r][c + 1][0], dp[r][c][1]]

                    if curr_score + dp[r][c + 1][0] == dp[r][c][0]:
                        dp[r][c][1] += 1

                if r < rows - 1 and dp[r + 1][c][1] > 0:
                    if curr_score + dp[r + 1][c][0] > dp[r][c][0]:
                        dp[r][c] = [curr_score + dp[r + 1][c][0], dp[r + 1][c][1]]

                    if curr_score + dp[r + 1][c][0] == dp[r][c][0]:
                        dp[r][c][1] += 1

                if r < rows - 1 and c < cols - 1 and dp[r + 1][c + 1][1]:
                    if curr_score + dp[r + 1][c + 1][0] > dp[r][c][0]:
                        dp[r][c] = [
                            curr_score + dp[r + 1][c + 1][0],
                            dp[r + 1][c + 1][1],
                        ]

                    if curr_score + dp[r + 1][c + 1][0] == dp[r][c][0]:
                        dp[r][c][1] += 1

        return dp[0][0]
