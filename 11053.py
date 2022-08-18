import sys
dp = [1]*1001
n = int(sys.stdin.readline())

A = list(map(int,sys.stdin.readline().split()))

for i in range(n):
    for j in range(i+1):
        if(A[i]>A[j]):
            dp[i] = max(dp[i],dp[j]+1)
max_num = 0
for i in range(n):
    max_num = max(max_num,dp[i])
print(max_num)




