class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0], reverse=True)
        s = 0
        n = len(costs)
        half = n / 2
        for i in range(n):
            if i < half:
                s += costs[i][0]
            else:
                s += costs[i][1]
        return s

