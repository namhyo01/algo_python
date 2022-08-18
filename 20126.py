import sys
input = sys.stdin.readline

n,m,s = map(int, input().split())


time = []

#0~n-1사이에 시험
def solve():
    for i in range(0,n-1):
        if(time[i+1][0]-(time[i][0]+time[i][1])>=m):
            return time[i][0]+time[i][1]

def last():
    if s-(time[-1][0] + time[-1][1])>=m:
        return time[-1][0] + time[-1][1]

for _ in range(n):
    x,y = map(int, input().split())
    time.append((x,y))
time.sort()

if time[0][0] >= m:
    print(0)
elif solve()!=None:
    print(solve())
elif last() != None:
    print(last())
else:
    print(-1)