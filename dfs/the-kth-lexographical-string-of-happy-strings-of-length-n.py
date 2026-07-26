class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy_strings = []
        def dfs(curr):
            if len(curr) >= n:
                happy_strings.append(curr)
                return
            
            for s in ['a', 'b', 'c']:
                if not curr:
                    dfs(s)

                elif curr[-1] != s:
                    dfs(curr + s)

        
        dfs('')
        return happy_strings[k - 1] if k - 1 < len(happy_strings) else ''