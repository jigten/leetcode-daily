from typing import List

def minNumberOfSeconds(mountainHeight: int, workerTimes: List[int]) -> int:
    def canReduce(seconds):
        total_reduction = 0

        for wt in workerTimes:
            l, r = 0, mountainHeight + 1

            while l < r:
                m = l + (r - l) // 2
                if wt * (m * (m + 1) // 2) > seconds:
                    r = m
                else:
                    l = m + 1

            total_reduction += r - 1
        
        return total_reduction >= mountainHeight

    l, r = 0, max(workerTimes) * (mountainHeight * (mountainHeight + 1) // 2)
    while l < r:
        m = l + (r - l) // 2

        if canReduce(m):
            r = m
        else:
            l = m + 1
        
    return r