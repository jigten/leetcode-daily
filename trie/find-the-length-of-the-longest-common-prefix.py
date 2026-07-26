from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = defaultdict(TrieNode)
        self.is_end = False


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = TrieNode()

        for num in arr1:
            node = root
            for d in str(num):
                node = node.children[d]

            node.is_end = True

        res = 0

        for num in arr2:
            curr = 0
            node = root
            for d in str(num):
                if d not in node.children:
                    break

                curr += 1
                node = node.children[d]

            res = max(res, curr)

        return res
