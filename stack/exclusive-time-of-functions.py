from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        res = [0] * n

        for l in logs:
            id, event, time = l.split(":")
            id, time = int(id), int(time)

            if event == "start":
                stack.append((id, time))
            else:
                _, start_time = stack.pop()
                res[int(id)] += int(time) - int(start_time)

        return res
