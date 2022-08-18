import sys
k = int(sys.stdin.readline())
dot = []
for i in range(k):
    [a,b] = map(int, sys.stdin.readline().split())
    dot.append([b,a])
dot.sort(key=lambda x: (x[0],x[1]))
for i in range(len(dot)):
    print(dot[i][1],end=' ')
    print(dot[i][0])
