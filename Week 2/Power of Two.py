class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and n & (n - 1) == 0

n=218
s = Solution()
ans=s.isPowerOfTwo(n)
print(ans)