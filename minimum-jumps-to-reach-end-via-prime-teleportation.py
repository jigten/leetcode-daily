from collections import defaultdict, deque
from typing import List

MAX_VAL = 10**6 + 1
spf = list(range(MAX_VAL))

for i in range(2, int(MAX_VAL**0.5) + 1):
    if spf[i] == i:
        for j in range(i * i, MAX_VAL, i):
            if spf[j] == j:
                spf[j] = i


class Solution:
    def minJumps(self, nums: List[int]) -> int:

        prime_to_idxs = defaultdict(list)

        for i, n in enumerate(nums):
            val = n

            while val > 1:
                prime = spf[val]
                prime_to_idxs[prime].append(i)

                while val % prime == 0:
                    val //= prime

        q = deque([(0, 0)])
        n = len(nums)
        seen_idxs = {0}
        seen_primes = set()

        while q:
            i, jumps = q.popleft()

            if i == n - 1:
                return jumps

            for nbr in [i - 1, i + 1]:
                if nbr not in seen_idxs and 0 <= nbr < n:
                    seen_idxs.add(nbr)
                    q.append((nbr, jumps + 1))

            num = nums[i]

            if spf[num] == num and num not in seen_primes:
                seen_primes.add(num)
                teleport_dest = prime_to_idxs[num]

                for tidx in teleport_dest:
                    if tidx not in seen_idxs:
                        seen_idxs.add(tidx)
                        q.append((tidx, jumps + 1))

        return -1
