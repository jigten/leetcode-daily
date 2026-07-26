from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()

        for word in wordDict:
            node = root
            for c in word:
                node = node.children[c]
            node.is_end = True

        memo = {}

        def dp(start):
            if start == len(s):
                return True

            if start in memo:
                return memo[start]

            node = root
            for i in range(start, len(s)):
                char = s[i]

                if char not in node.children:
                    break

                node = node.children[char]

                if node.is_end:
                    if dp(i + 1):
                        memo[start] = True
                        return True
            memo[start] = False
            return False

        return dp(0)

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            if not dp[i - 1]:
                continue

            node = root

            for j in range(i, n + 1):
                if s[j - 1] not in node.children:
                    continue

                node = node.children[s[j - 1]]

                if node.is_end:
                    dp[j] = True

        return dp[n]


solution = Solution()
assert solution.wordBreak(s="leetcode", wordDict=["leet", "code"]) == True
assert solution.wordBreak(s="applepenapple", wordDict=["apple", "pen"]) == True
assert (
    solution.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
    == False
)
