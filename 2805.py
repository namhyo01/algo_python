import sys

N,M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
l,r = 0,1000000000
res = 0
while l<=r:
    mid = (l+r)//2
    tot = 0
    for t in trees:
        if(mid<t):
            tot+=t-mid
        if(tot>=M):
            break
    if(tot>=M):
        res = mid
        l = mid+1
    else:
        r = mid-1
print(res)
