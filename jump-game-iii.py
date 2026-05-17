from typing import List
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = deque([start])
        seen = {start}

        while q:
            idx = q.popleft()

            if arr[idx] == 0:
                return True

            for ni in [idx + arr[idx], idx - arr[idx]]:
                if 0 <= ni < n and ni not in seen:
                    seen.add(ni)
                    q.append(ni)

        return False
