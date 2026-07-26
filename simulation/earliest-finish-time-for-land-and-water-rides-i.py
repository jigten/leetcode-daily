from typing import List


class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int],
    ) -> int:
        res = 10**9

        for ls, ld in zip(landStartTime, landDuration):
            for ws, wd in zip(waterStartTime, waterDuration):
                et = ls + ld

                if et >= ws:
                    res = min(res, et + wd)
                else:
                    res = min(res, ws + wd)


        for ws, wd in zip(waterStartTime, waterDuration):
            for ls, ld in zip(landStartTime, landDuration):
                et = ws + wd

                if et >= ls:
                    res = min(res, et + ld)
                else:
                    res = min(res, ls + ld)

        return res
