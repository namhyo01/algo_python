
def sugar(n):
    for x in range(n//3+1):
        for y in range(n//5+1):
            if ((3*x + 5*y) == n):
                print(x+y)
                return
    print(-1)
    return

n = int(input())
sugar(n)