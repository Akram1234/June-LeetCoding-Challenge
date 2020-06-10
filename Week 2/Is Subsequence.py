class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        n = len(s)
        for i in range(len(t)):
            if j<n and t[i] == s[j]:
                j+=1
        return j==n

s = "agc"
t = "ahbgdc"
ans = Solution().isSubsequence(s,t)
print(ans)