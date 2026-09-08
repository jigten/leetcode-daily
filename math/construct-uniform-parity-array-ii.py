class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)

        even_cnt, smallest = 0, float('inf')

        for num in nums1:
            if num % 2 == 0:
                even_cnt += 1
            
            smallest = min(smallest, num)
        
        if smallest % 2:
            return True
        
        return even_cnt == n
        
