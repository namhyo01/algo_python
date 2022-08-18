T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    human = [m for m in range(1,n+1)] # 1층 사람들
    for __ in range(k):
        for k in range(1,n):
            human[k] += human[k-1]
    print(human[-1])