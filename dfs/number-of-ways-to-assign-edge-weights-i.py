from collections import defaultdict
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(n, p):
            max_depth = 0
            for child in adj[n]:
                if child == p: continue # avoid infinite looping between parent and child
                max_depth = max(dfs(child, n) + 1, max_depth)

            return max_depth

        max_depth = dfs(1, -1)
        return (2 ** (max_depth - 1)) % (10**9 + 7)
