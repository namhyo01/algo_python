num = [0] * 42

for i in range(10):
    a = int(input())%42
    num[a] = num[a]+1
cnt = 0
for i in range(42):
    if num[i]>0:
        cnt = cnt+1

print(cnt)

