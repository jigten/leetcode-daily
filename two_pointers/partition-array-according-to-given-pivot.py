from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        l, r = 0, n - 1
        res = [0] * n

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1

            if nums[j] > pivot:
                res[r] = nums[j]
                r -= 1


        while l <= r:
            res[l] = pivot
            l += 1

        return res

        before, after = [], []
        cnts = 0

        for n in nums:
            if n < pivot:
                before.append(n)
            elif n > pivot:
                after.append(n)
            else:
                cnts += 1


        return before + [pivot] * cnts + after
