import sys
n = int(sys.stdin.readline())
members = []
for i in range(n):
    a,b = map(str, sys.stdin.readline().split())
    members.append([int(a),i,b])
members.sort(key=lambda x: (x[0],x[1]))
for a,b,c in members:
    print(a,c)

