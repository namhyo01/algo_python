import sys
import math
input = sys.stdin.readline

n, k = map(int,input().split())
V = []
V = list(map(int, input().split()))

ans = 999999999999999999999999999
while(k<=n):
    for i in range(n-k+1):
        num = V[i:i+k]
        m = sum(num)/k
        der = 0
        for j in num:
            der += (j-m)**2
        der /= k
        ans = min(ans,math.sqrt(der))
    k+=1
print('{:.11f}'.format(ans))