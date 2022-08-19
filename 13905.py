
import sys
from collections import deque

visited = [False]*100001
def bfs(cnt,s,e,house):
    global visited
    queue = deque()
    queue.append(s)
    visited[s] = True
    while queue:
        cur = queue.popleft()
        if(cur == e):
            return True
        for i in range(len(house[cur])):
            nh = house[cur][i][0]
            cost = house[cur][i][1]
            if(cost>=cnt and not visited[nh]):
                queue.append(nh)
                visited[nh] = True

    return False

N,M = map(int,sys.stdin.readline().split())
s,e = map(int,sys.stdin.readline().split())
house = [[] for _ in range(M)]
maxCost = 0
for _ in range(M):
    h1,h2,k = map(int,sys.stdin.readline().split())
    house[h1].append([h2,k])
    house[h2].append([h1,k])
    maxCost = max(maxCost,k)

l,h = 1, maxCost
ans = 0
while l<=h:
    mid = (l+h)//2
    visited = [False]*100001
    if(bfs(mid,s,e,house)):
        ans = mid
        l = mid+1
    else:
        h = mid-1

print(ans)