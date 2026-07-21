class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        seen = set()
        ch_to_idx = {}

        for i, c in enumerate(s):
            ch_to_idx[c] = i

        for i, c in enumerate(s):
            if c in seen:
                continue

            while stack and ord(stack[-1]) > ord(c) and ch_to_idx[stack[-1]] > i:
                rem = stack.pop()
                seen.remove(rem)

            seen.add(c)
            stack.append(c)

        return "".join(stack)
