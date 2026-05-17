from typing import List


class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        sum_of_all_milestones, max_milestone = sum(milestones), max(milestones)

        if sum_of_all_milestones - max_milestone >= max_milestone:
            return sum_of_all_milestones

        return 2 * (sum_of_all_milestones - max_milestone) + 1

