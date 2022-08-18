cnt = 0
N = int(input())
for i in range(1,N+1):
    _cnt = 0
    ## 숫자가 한개이거나 2개일때는 항상 통과
    if ((len(str(i)) == 1) or len(str(i)) == 2):
        cnt+=1
    else:
        right = True
        k = []
        for j in str(i):
            k.append(int(j))
        temp = k[0] - k[1]
        for l in range(1,len(str(i))-1):
            if temp != (k[l]-k[l+1]):
                right = False
                break
        if right:
            cnt += 1
print(cnt)

            
        



