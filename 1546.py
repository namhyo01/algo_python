a = int(input())

num = list(map(int, input().split()))

max_score = max(num)
avg = 0
for i in range(a):
    avg = avg + ((num[i]/max_score)*100)

print(round(avg/a,2))

