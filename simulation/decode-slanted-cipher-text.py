class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols = len(encodedText) // rows
        mat = [[''] * cols for _ in range(rows)]

        i = 0
        for r in range(rows):
            for c in range(cols):
                mat[r][c] = encodedText[i]
                i += 1
        
        res = ''
        for col in range(cols):
            cr = 0
            cc = col
            while cr < rows and cc < cols:
                res += mat[cr][cc]
                cr += 1
                cc += 1

        return res.rstrip()

solution = Solution()
print(solution.decodeCiphertext(encodedText = "ch   ie   pr", rows = 3))
print(solution.decodeCiphertext(encodedText = "iveo    eed   l te   olc", rows = 4))
print(solution.decodeCiphertext(encodedText = "coding", rows = 1))