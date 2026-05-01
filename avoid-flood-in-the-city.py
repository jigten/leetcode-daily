"""
1488. Avoid Flood in The City
Medium

Your country has 10^9 lakes. Initially, all the lakes are empty, but when it rains over the nth lake, 
the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. 
Your goal is to avoid floods in any lake.

Given an integer array rains where:
- rains[i] > 0 means there will be rains over the rains[i] lake.
- rains[i] == 0 means there are no rains this day and you must choose one lake this day and dry it.

Return an array ans where:
- ans.length == rains.length
- ans[i] == -1 if rains[i] > 0.
- ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.

If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

Example 1:
Input: rains = [1, 2, 3, 4]
Output: [-1, -1, -1, -1]

Example 2:
Input: rains = [1, 2, 0, 0, 2, 1]
Output: [-1, -1, 2, 1, -1, -1]  # One possible answer

Example 3:
Input: rains = [1, 2, 0, 1, 2]
Output: []

Constraints:
- 1 <= rains.length <= 10^5
- 0 <= rains[i] <= 10^9
"""
import bisect

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        res = [1] * n
        sunny_days = []
        mapping = {}
        
        for day, lake in enumerate(rains):
            if lake == 0:
                sunny_days.append(day)
            else:
                res[day] = -1
                if lake in mapping:
                    target_day = bisect.bisect(sunny_days, mapping[lake])
                    if target_day == len(sunny_days):
                        return []
                    res[sunny_days[target_day]] = lake 
                    del sunny_days[target_day]
                
                mapping[lake] = day

        return res


def test_avoid_flood():
    solution = Solution()

    # Test case 1
    rains1 = [1, 2, 3, 4]
    expected1 = [-1, -1, -1, -1]
    result1 = solution.avoidFlood(rains1)
    print(f"Test 1: {result1} == {expected1} -> {result1 == expected1}")
    
    # Test case 2
    rains2 = [1, 2, 0, 0, 2, 1]
    expected2 = [-1, -1, 2, 1, -1, -1]  # One possible answer
    result2 = solution.avoidFlood(rains2)
    print(f"Test 2: {result2}")
    
    # Test case 3
    rains3 = [1, 2, 0, 1, 2]
    expected3 = []
    result3 = solution.avoidFlood(rains3)
    print(f"Test 3: {result3} == {expected3} -> {result3 == expected3}")


if __name__ == "__main__":
    test_avoid_flood()
