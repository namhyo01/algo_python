import sys

result = {'C':0,'H':0,'O':0}
eachCnt = []
chemical = sys.stdin.readline().rstrip()
M = chemical.replace('+', ' ').replace('=',' ').split(' ') # 일단 분해하고보자

def solve():
    global eachCnt
    word = ['C','H','O']
    for i in range(1,11):
        for j in range(1,11):
            for k in range(1,11):
                cnt = 0
                for w in word:
                    if(eachCnt[0][w]*i + eachCnt[1][w]*j == eachCnt[2][w]*k):
                        cnt+=1
                if(cnt == 3):
                    print(i,j,k,sep=' ')
                    return

for m in M:
    temp = {'C':0,'H':0,'O':0}
    for i in range(len(m)):
        if(m[i]=='C'):
            if( i != len(m)-1 and m[i+1].isdigit()):
                temp[m[i]]+=int(m[i+1])
            else:
                temp[m[i]]+=1
        elif(m[i]=='H'):
            if(i != len(m)-1 and m[i+1].isdigit()):
                temp[m[i]]+=int(m[i+1])
            else:
                temp[m[i]]+=1
        elif(m[i]=='O'):
            if(i != len(m)-1 and m[i+1].isdigit()):
                temp[m[i]]+=int(m[i+1])
            else:
                temp[m[i]]+=1
    eachCnt.append(temp)
solve()




                
