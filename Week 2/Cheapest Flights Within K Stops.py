import heapq
from typing import List


class Graph():
    def __init__(self,n):
        self.v= n
        self.g =[[] for __ in range(n)]
    def add(self,u,v,w):
        self.g[u].append([v,w])

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        o = Graph(n)
        for u,v,w in flights:
            o.add(u,v,w)
        q=[]
        heapq.heappush(q,[0,src,K+1])
        while q:
            p, c, s = heapq.heappop(q)
            if c==dst:
                return p
            if s>0:
                for neigh, cost in o.g[c]:
                    heapq.heappush(q, [p+cost, neigh, s-1])
        return -1

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
ans = Solution().findCheapestPrice(n,flights,src,dst,k)
print(ans)



