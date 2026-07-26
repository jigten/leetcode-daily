from collections import defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def findMaxPathScore(
        self, edges: List[List[int]], online: List[bool], k: int
    ) -> int:
        adj = defaultdict(list)
        l_cost, r_cost = float("inf"), float("-inf")

        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                l_cost = min(l_cost, cost)
                r_cost = max(r_cost, cost)

        def pathExists(m_cost):
            @lru_cache(None)
            def dfs(node) -> int:
                if node == len(online) - 1:
                    return 0

                cost = float("inf")
                for child, c_cost in adj[node]:
                    if c_cost < m_cost:
                        continue

                    cost = min(cost, dfs(child) + c_cost)

                return cost

            return dfs(0) <= k

        res = -1

        while l_cost <= r_cost:
            m_cost = l_cost + (r_cost - l_cost) // 2

            if pathExists(m_cost):
                res = m_cost
                l_cost = m_cost + 1
            else:
                r_cost = m_cost - 1

        return res
