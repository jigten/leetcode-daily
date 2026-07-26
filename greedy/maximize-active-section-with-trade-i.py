class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        one_count = s.count("1")
        segments, curr_seg = [], 0

        for c in s:
            if c == "1":
                if curr_seg > 0:
                    segments.append(curr_seg)
                curr_seg = 0
            else:
                curr_seg += 1

        if curr_seg > 0:
            segments.append(curr_seg)

        if not segments:
            return one_count

        if len(segments) < 2:
            return one_count

        n = len(segments)
        max_adj_seg = max(s1 + s2 for s1, s2 in zip(segments[: n - 1], segments[1:]))

        return one_count + max_adj_seg
