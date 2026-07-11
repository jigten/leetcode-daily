from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        seen = set()
        res = 0

        def dfs(node, comp_nodes):
            for nbr in adj[node]:
                if nbr in seen:
                    continue
                seen.add(nbr)
                comp_nodes.append(nbr)
                dfs(nbr, comp_nodes)

        for i in range(n):
            if i in seen:
                continue

            seen.add(i)
            comp_nodes = [i]
            dfs(i, comp_nodes)

            node_cnt = len(comp_nodes)
            edge_cnt = sum(len(adj[node]) for node in comp_nodes) // 2

            if edge_cnt == (node_cnt * (node_cnt - 1) // 2):
                res += 1

        return res
