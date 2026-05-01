class Fancy:
    def __init__(self):
        self.seq = []
        self.mod = 10**9 + 7
        self.add = 0
        self.mult = 1
        
    def append(self, val: int) -> None:
        s = (val - self.add) * pow(self.mult, self.mod - 2, self.mod) % self.mod
        self.seq.append(s)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.mod

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % self.mod
        self.mult = (self.mult * m) % self.mod

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.mod