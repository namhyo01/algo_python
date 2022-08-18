k = int(input())
dot = []
for i in range(k):
    x = list(map(int, input().split()))
    dot.append(x)
dot.sort(key=lambda x: (x[0],x[1]))
for i in range(len(dot)):
    print(dot[i][0],end=' ')
    print(dot[i][1])
