star = '*'
n = int(input())
for j in range(1, n+1):
    for k in range(j):
        print('*', end= '')
    print()
for j in range(n-1, 0,-1):
    for k in range(j):
        print('*', end = '')
    print()

