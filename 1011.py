import math
T = int(input())

for i in range(T):
    x,y = map(int,input().split())
    count = 0
    dis = y-x
    n = int(math.sqrt(dis))
    _n = n+1
    if n == 1:
        print(dis)
        continue
    elif (n*_n+1) <= dis:
        print(n+_n)
    elif (n*n+1)<=dis:
        print(2*n)
    else:
        print(2*n-1)