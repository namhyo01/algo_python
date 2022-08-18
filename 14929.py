n = int(input())
x = list(map(int,input().split(' ')))
ans = 0
sum = 0 
for i in range(n):
    ans += x[i] * sum
    sum += x[i]

print(ans)