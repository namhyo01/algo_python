import sys
N,C = map(int,sys.stdin.readline().split())
mac = []
for _ in range(N):
    mac.append(int(sys.stdin.readline()))
mac.sort()
l,r=1,mac[-1]-mac[0]
while l<=r:
    mid = (l+r)//2
    first = mac[0]
    cnt = 0
    for m in mac:
        if m-first >= mid:
            cnt+=1
            first = m
    if cnt >= C-1:
        l = mid+1
    else:
        r = mid-1

print(l)