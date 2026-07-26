from collections import defaultdict, deque
from typing import List


class Solutionum:
    def minumJumps(self, arr: List[int]) -> int:
        n = len(arr)
        adj = defaultdict(list)

        for i, num in enumerate(arr):
            adj[num].append(i)
          
        q = deque([(0, 0)])
        seen = {0}

        while q:
            idx, dist = q.popleft()

            if idx == n - 1:
                return dist

            if idx + 1 < n and idx + 1 not in seen:
                seen.add(idx + 1)
                q.append((idx + 1, dist + 1))

            if idx - 1 >= 0 and idx - 1 not in seen:
                seen.add(idx - 1)
                q.append((idx - 1, dist + 1))

            moves = adj[arr[idx]]
            for m in moves:
                if m not in seen:
                    seen.add(m)
                    q.append((m, dist + 1))
            adj[arr[idx]] = []

        return -1
