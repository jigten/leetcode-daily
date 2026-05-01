from typing import List
from collections import defaultdict

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        adj = defaultdict(list)

        for i, j in allowedSwaps:
            adj[i].append(j)
            adj[j].append(i)
        
        seen = set()
        res = len(source)

        def dfs(idx, source_counts, target_counts):
            conns = adj[idx] or [idx]
            for i in conns:
                if i in seen:
                    continue
                seen.add(i)
                source_counts[source[i]] += 1
                target_counts[target[i]] += 1
                dfs(i, source_counts, target_counts)

        for idx in range(len(source)):
            if idx in seen:
                continue

            source_counts, target_counts = defaultdict(int), defaultdict(int)
            dfs(idx, source_counts, target_counts)
            common_matches = 0
            for val in source_counts.keys():
                common_matches += min(source_counts[val], target_counts[val])
            
            res -= common_matches
        
        return res

solution = Solution()
assert(solution.minimumHammingDistance(source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]) == 1)
assert(solution.minimumHammingDistance(source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []) == 2)
assert(solution.minimumHammingDistance(source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]) == 0)

