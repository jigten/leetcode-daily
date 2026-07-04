from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a, b, dist in roads:
            adj[a].append((b, dist))
            adj[b].append((a, dist))

        seen = set([1])
        res = float("inf")

        def dfs(node):
            nonlocal res

            for child, dist in adj[node]:
                res = min(res, dist)

                if child not in seen:
                    seen.add(child)
                    dfs(child)

        dfs(1)
        return res
