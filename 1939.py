import sys
from collections import deque

visited = [False]*100001
def bfs(cnt,start,finish,bridge):
    global visited
    pq = deque()
    pq.append(start)
    visited[start] = True
    while pq:
        cur = pq.popleft()
        if(cur==finish):
            return True
            
        for i in range(len(bridge[cur])):
            go = bridge[cur][i][0]
            cost = bridge[cur][i][1]
            if(cnt <= cost and not visited[go]):
                visited[go]=True
                pq.append(go)
    return False



N, M = map(int,sys.stdin.readline().split())
bridge = [[] for _ in range(100001)]

maxCost = 0
for _ in range(M):
    A,B,C = map(int,sys.stdin.readline().split())
    bridge[A].append([B,C])
    bridge[B].append([A,C])
    maxCost = max(maxCost,C)
start,finish = map(int,sys.stdin.readline().split())
l, h = 0, maxCost
while l<=h:
    mid = (l+h)//2
    visited = [False]*100001
    if(bfs(mid,start,finish,bridge)):
        l = mid+1
    else:
        h = mid-1
    
print(h)
    