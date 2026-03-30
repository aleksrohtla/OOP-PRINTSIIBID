import random

class Generator:
    def generate(self, n):
        return [random.randint(1, 9) for _ in range(n)]

class Splitter:
    def split(self, m):
        n = len(m)
        diag1 = [m[i][i] for i in range(n)]
        diag2 = [m[i][n-1-i] for i in range(n)]
        return m + [list(col) for col in zip(*m)] + [diag1, diag2]

class Verifier:
    def verify(self, parts):
        return len(set(map(sum, parts))) == 1 if parts else True

class MagicSquareGenerator:
    def __init__(self):
        self.g, self.s, self.v = Generator(), Splitter(), Verifier()

    def generate(self, size):
        while True:
            nums = self.g.generate(size * size)
            matrix = [nums[i:i + size] for i in range(0, len(nums), size)]
            if self.v.verify(self.s.split(matrix)):
                return matrix

gen = MagicSquareGenerator()
for row in gen.generate(3):
    print(row)