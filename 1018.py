def chess(table):
    c1 = 0
    c2 = 0
    for i in range(8): #첫 글자가 B
        for j in range(8):
            x = 0 if i%2==0 else 1
            y = 0 if j%2==0 else 1
            if(x==0 and y==0) or (x==1 and y==1):
                if table[i][j] != 'B':
                    c1 +=1
            if(x==0 and y==1) or (x==1 and y==0):
                if table[i][j] != 'W':
                    c1+=1
    for i in range(8):#첫글자가 W
        for j in range(8):
            x = 0 if i%2==0 else 1
            y = 0 if j%2==0 else 1
            if(x==0 and y==0) or (x==1 and y==1):
                if table[i][j] != 'W':
                    c2 +=1
            if(x==0 and y==1) or (x==1 and y==0):
                if table[i][j] != 'B':
                    c2+=1    
    return min(c1,c2)
N, M = map(int, input().split())
table = [list(input())for i in range(N)]
rewrite = []
for i in range(N-7):
    for j in range(M-7):
        re_table = [temp[0+j:8+j] for temp in table[0+i:8+i]]
        rewrite.append(chess(re_table))
print(min(rewrite))