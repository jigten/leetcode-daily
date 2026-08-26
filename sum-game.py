class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        lSum = lCnt = rSum = rCnt = 0
        m = n // 2

        for i in range(m):
            ch = num[i]
            if ch == "?":
                lCnt += 1
            else:
                lSum += int(ch)

        for i in range(m, n):
            ch = num[i]
            if ch == "?":
                rCnt += 1
            else:
                rSum += int(ch)

        print(lSum, lCnt, rSum, rCnt)

        # if odd places to change, then Alice can always win with her final move
        if (lCnt + rCnt) % 2:
            return True

        # if equal places to change on both sides, Alice can win if the inial diff isn't equal
        if lCnt == rCnt:
            return (lSum - rSum) != 0

        # if uneven counts of question marks, we would have a surplus s question marks that Bob can't match with Alice move
        # Bob can only win if the diff of the sums is 9 * the mid of surplus
        # for one surplus pair 2 -> m = 2 // 2 = 1, Bob can only win if the sum diff is 9 where Alice will play anything between 0-9 and Bob can simply play 9 - Alice chosen digit e.g. is Alice chose 8 Bob can place 1

        if lCnt > rCnt:
            mid = (lCnt - rCnt) // 2
            return (lSum - rSum) != -9 * mid

        if rCnt > lCnt:
            mid = (rCnt - lCnt) // 2
            return (lSum - rSum) != 9 * mid

        return False
