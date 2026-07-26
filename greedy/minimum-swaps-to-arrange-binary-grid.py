
from typing import List

def minSwaps(grid: List[List[int]]) -> int:
    row_to_max_r = [-1] * len(grid)

    for i, row in enumerate(grid):
        max_r = -1
        for j, c in enumerate(row):
            if c == 1:
                max_r = j 
        
        row_to_max_r[i] = max_r
    
    cost = 0

    for i in range(len(grid)):
        for j in range(i, len(grid)):
            if row_to_max_r[j] <= i:
                for k in range(j, i, -1):
                    row_to_max_r[k], row_to_max_r[k - 1] = row_to_max_r[k - 1], row_to_max_r[k]
            
                cost += j - i
                break
        else:
            return -1
    
    return cost
