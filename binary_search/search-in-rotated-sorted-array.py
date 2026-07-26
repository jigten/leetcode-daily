from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target: return m

            # check left side is sorted
            if nums[l] <= nums[m]:
                # we can confirm check if target is in the sorted range on the left
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # check if right side is sorted
            elif nums[m] <= nums[r]:
                # we can confirm check if target is in the sorted range on the right
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
