import sys
N = int(sys.stdin.readline())
dp=[0]*10002
podoju = [0]*10002
for i in range(1,N+1):
    podoju[i] = int(sys.stdin.readline())

dp[1] = podoju[1]
dp[2] = podoju[2]+podoju[1]
i=3
while(i<=N):
    dp[i] = max(dp[i-2]+podoju[i],dp[i-3]+podoju[i-1]+podoju[i])
    dp[i] = max(dp[i],dp[i-1])  # 안마시는게 이득인 경우
    i+=1

print(dp[N])
