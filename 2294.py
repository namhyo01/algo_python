import sys

n,k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
dp = [9999999]*100001
dp[0] = 0
for i in coins:
    for j in range(i,k+1):
        dp[j] = min(dp[j-i]+1,dp[j])

if dp[k]==9999999:
    print(-1)
else:
    print(dp[k])