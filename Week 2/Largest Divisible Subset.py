
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==0:
            return []
        nums.sort(reverse=True)
        l = [1 for _ in range(n)]
        p = [-1 for _ in range(n)]
        idx = 0
        for i in range(1,n):
            for j in range(0,i):
                if nums[j]%nums[i]==0 and l[i]<l[j]+1:
                    l[i]=l[j]+1
                    p[i]=j
            if l[idx]<l[i]:
                idx=i
        ans = []
        while idx>=0:
            ans.append(nums[idx])
            idx = p[idx]
        return ans
