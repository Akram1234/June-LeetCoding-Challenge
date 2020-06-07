#verison 4
def coin_change(amount, coins):
    n = len(coins)
    dp=[[0 for _ in range(amount+1)] for i in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        dp[i][0] = 1
        for j in range(1,amount+1):
            dp[i][j]+=dp[i-1][j]
            if (j - coins[i - 1] >= 0):
                dp[i][j] += dp[i][j - coins[i - 1]]
    return dp[n][amount]


amount =5
coins = [1,2,3]
ans = coin_change(amount, coins)
print(ans)

# version 3 --> result : all test cases passed but TLE(taken more time)
# def coin_change(amount, coins):
#     n = len(coins)
#     dp=[0 for _ in range(amount+1)]
#     for i in range(n+1):
#         temp = [0 for _ in range(amount+1)]
#         for j in range(amount+1):
#             s = 0
#             if j==0:
#                 s=1
#             elif i!=0:
#                 k=0
#                 while(j-k*coins[i-1]>=0):
#                     s+=dp[j-k*coins[i-1]]
#                     k+=1
#             temp[j]=s
#         dp=temp
#     return dp[amount]


#version 2 --> result : all test cases passed but TLE(taken more time)
# def coin_change(amount, coins):
#     n = len(coins)
#     dp=[[0 for _ in range(amount+1)] for i in range(n+1)]
#     for i in range(n+1):
#         for j in range(amount+1):
#             if j==0:
#                 dp[i][j]=1
#             elif i!=0:
#                 k=0
#                 while(j-k*coins[i-1]>=0):
#                     dp[i][j]+=dp[i-1][j-k*coins[i-1]]
#                     k+=1
#     return dp[n][amount]

# version 1 --> result : all test cases passed but TLE(taken more time)
# def coin_change(amount, coins):
#     def coin_change_util(i,j):
#         s= 0
#         if dp[i][j]==0:
#             if j==0:
#                 s=1
#             elif i!=0:
#                 k=0
#                 while(j-k*coins[i-1]>=0):
#                     s+=coin_change_util(i-1,j-k*coins[i-1])
#                     k+=1
#             dp[i][j]=s
#         return dp[i][j]
#
#     n = len(coins)
#     dp=[[0 for _ in range(amount+1)] for i in range(n+1)]
#     return coin_change_util(n, amount)