import sys
from collections import defaultdict
from math import inf
input = sys.stdin.readline

n,m = map(int, input().split())
cost = [[inf]*(n) for _ in range(n+1)]
print(cost)
for _ in range(m):
    a,b = map(int, input().split())
    cost[a][b] = 1
    cost[b][a] = 1
for k in range(1,n+1):
    cost[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])
max = inf  
  
for i in range(1,n):
    for j in range(2,n+1):
        tmp = 0
        for k in range(1,n+1):
            tmp += min(cost[k][i], cost[k][j])
        if max>tmp:
            max = tmp
            ans = [i,j,2*tmp]
print(*ans)


