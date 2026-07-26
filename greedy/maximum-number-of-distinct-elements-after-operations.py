"""
3397. Maximum Number of Distinct Elements After Operations
Difficulty: Medium

You are given an integer array nums and an integer k.

You are allowed to perform the following operation on each element of the array at most once:
Add an integer in the range [-k, k] to the element.

Return the maximum possible number of distinct elements in nums after performing the operations.

Example 1:

Input: nums = [1,2,2,3,3,4], k = 2
Output: 6
Explanation: nums changes to [-1, 0, 1, 2, 3, 4] after performing operations on the first four elements.

Example 2:

Input: nums = [4,4,4,4], k = 1
Output: 3
Explanation: By adding -1 to nums[0] and 1 to nums[1], nums changes to [3, 5, 4, 4].

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= k <= 10^9
"""

def maximumDistinctElements(nums, k):
    n = len(nums)
    nums.sort()
    
    # Track the last assigned value to ensure uniqueness
    last_assigned = float('-inf')
    count = 0
    
    for num in nums:
        # For current number, we can assign any value in [num - k, num + k]
        # We want the smallest possible value that's > last_assigned
        min_possible = max(num - k, last_assigned + 1)
        max_possible = num + k
        
        # If we can assign a valid value
        if min_possible <= max_possible:
            last_assigned = min_possible
            count += 1
        # If not, we skip this element (can't make it distinct)
    
    return count

# Basic test cases
if __name__ == "__main__":
    print(maximumDistinctElements([1,2,2,3,3,4], 2))  # Expected: 6
    print(maximumDistinctElements([4,4,4,4], 1))      # Expected: 3