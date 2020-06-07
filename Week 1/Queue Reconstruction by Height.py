from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key = lambda x: (-x[0],x[1]))
        for p in people:
            res.insert(p[1], p)
        return res


people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
s = Solution()
ans=s.reconstructQueue(people)
print(ans)
