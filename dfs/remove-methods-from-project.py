from collections import defaultdict
from typing import List


class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        adj = defaultdict(list)
        seen = set([k])

        for a, b in invocations:
            adj[a].append(b)

        def dfs(m):
            for c in adj[m]:
                if c in seen:
                    continue
                seen.add(c)
                dfs(c)

        dfs(k)

        for m in range(n):
            if m not in seen:
                for c in adj[m]:
                    if c in seen:
                        return list(range(n))

        return [m for m in range(n) if m not in seen]
