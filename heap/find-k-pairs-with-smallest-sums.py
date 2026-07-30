import heapq
from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        res = []
        h = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j], i, j))

        push(0, 0)

        while len(res) < k:
            _, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            push(i, j + 1)

            if j == 0:
                push(i + 1, 0)

        return res
