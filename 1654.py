import sys
K,N = map(int,sys.stdin.readline().split())
lan = []
for _ in range(K):
    lan.append(int(sys.stdin.readline()))
l,r = 1,999999999999999999999999
ans = 0

while l<=r:
    mid = int((l+r)/2)
    res = 0
    for i in lan:
        res += int(i/mid)
    if(res>=N):
        if(ans<mid):
            ans = mid
        l = mid+1
    else:
        r = mid-1
    
print(ans)
