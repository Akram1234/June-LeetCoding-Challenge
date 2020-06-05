from random import random


class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        self.s = 0
        for weight in w:
            self.s += weight
            self.weights.append(self.s)


    def pickIndex(self) -> int:
        n = random.randint(1, self.s)
        for i, w in enumerate(self.weights):
            if n <= w:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()