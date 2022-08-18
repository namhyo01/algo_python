
n = int(input())

star = []
for i in range(n):
    temp = list('*'*n)
    star.append(temp)

count = 0
temp = n
while temp!=1:
    temp = temp//3
    count += 1

for i in range(count):
    #빈칸 찾기
    blank = [k for k in range(n) if (k//3**i) %3 ==1]
    for l in blank:
        for m in blank:
            star[l][m] = ' '

for i in star:
    print("".join(i))

