n = int(input())
x = []
for i in range(n):
    a = list(map(int, input().split()))
    x.append(a)


for i in x:
    rank = 1
    for j in x:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')


    


    

