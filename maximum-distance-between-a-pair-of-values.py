from typing import List

class Solution:
    def search(self, arr, val, l, r):
        best_j = -1
        while l <= r:
            m = l + (r - l) // 2
            if arr[m] < val:
                r = m - 1
            else:
                best_j = m
                l = m + 1
        
        return best_j


    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        # binary search solution
        # for i, n1 in enumerate(nums1):
        #     j = self.search(nums2, n1, i, len(nums2) - 1)
        #     if j != -1:
        #         res = max(res, j - i)
        
        # linear solution
        i, j = 0, 1
        m, n = len(nums1), len(nums2)

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res = max(res, j - i)
                j += 1
            else:
                i += 1
        return res

solution = Solution()
assert(solution.maxDistance(nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]) == 2)
assert(solution.maxDistance(nums1 = [2,2,2], nums2 = [10,10,1]) == 1)
assert(solution.maxDistance(nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]) == 2)
