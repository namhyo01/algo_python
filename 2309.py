def find_small(a):
    total = sum(a)
    for i in range(8):
        for j in range(i+1,9):
            if(total-a[i]-a[j] == 100):
                for k in range(0,i):
                    print(a[k])
                for k in range(i+1,j):
                    print(a[k])
                for k in range(j+1,9):
                    print(a[k])
                return 0
            

b = list()
for i in range(9):
    temp = int(input())
    b.append(temp)
b.sort()
find_small(b)


