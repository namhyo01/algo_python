import math
T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    dis = math.sqrt((x2-x1)**2 + (y2-y1)**2) #중신간의 거리
    R = r1+r2
    if dis==0:
        if r1==r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    else:
        if dis == r1+r2 or dis==abs(r1-r2):
            print(1)
        elif dis < r1+r2 and dis > abs(r1-r2):
            print(2)
        else:
            print(0)

    