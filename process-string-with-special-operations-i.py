class Solution:
    def processStr(self, s: str) -> str:
        res = []

        for c in s:
            if c == "*":
                if len(res):
                    res.pop()
            elif c == "#":
                res += res
            elif c == "%":
                res = res[::-1]
            else:
                res.append(c)

        return "".join(res)
