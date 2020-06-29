class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m,n = m-1,n-1
        a,b = m,n
        if m>n:
            a=m
            b=n
        else:
            a=n
            b=m
        s=a+b
        nu,de = 1,1
        while(b>0):
            nu*=s
            de*=b
            s-=1
            b-=1
        return int(nu/de)
        
