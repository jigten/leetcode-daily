from typing import List


class UnionFind:
    def __init__(self, n) -> None:
        self.parents = list(range(n))

    def find(self, i):
        if self.parents[i] == i:
            return i

        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        root_i, root_j = self.find(i), self.find(j)
        if root_i != root_j:
            self.parents[root_i] = root_j


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        # Union find solution
        uf = UnionFind(n)
        res = []

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                uf.union(i - 1, i)

        for qa, qb in queries:
            if uf.find(qa) == uf.find(qb):
                res.append(True)
            else:
                res.append(False)

        return res

        # Connected components solution
        # connected_ids = [-1] * n
        # id = 0
        # connected_ids[0] = 0
        #
        # for i in range(1, n):
        #     if nums[i] - nums[i - 1] > maxDiff:
        #         id += 1
        #
        #     connected_ids[i] = id
        #
        # res = []
        #
        # for a, b in queries:
        #     if connected_ids[a] == connected_ids[b]:
        #         res.append(True)
        #     else:
        #         res.append(False)
        #
        # return res
