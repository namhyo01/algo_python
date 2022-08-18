import sys
input = sys.stdin.readline

maxNum,minNum = 0,999999999

#홀수 체크
def countOdd(num):
    
    cnt = 0
    for i in num:
        if(int(i)%2==1):
            cnt+=1
    return cnt

def solve(n,oddN):
    global maxNum,minNum
    if len(n)==1:
        maxNum = max(maxNum,oddN)
        minNum = min(minNum,oddN)
    elif len(n)==2:
        a,b = n[0],n[1]
        c = int(a)+int(b)
        solve(str(c),oddN+countOdd(str(c)))
    else:
        for i in range(len(n)-2):
            for j in range(i+1,len(n)-1):
                a = int(n[0:i+1])
                b = int(n[i+1:j+1])
                c = int(n[j+1:])
                d = a+b+c
                solve(str(d),oddN+countOdd(str(d)))


N = input().strip()
solve(N,countOdd(N))
print(maxNum,minNum)
