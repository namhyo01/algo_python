import sys
N = int(sys.stdin.readline())
count1 = 0
chess = [0]*15

def condition(i):
    for j in range(i):
        if(chess[i]==chess[j] or abs(chess[i]-chess[j])==(i-j)):
            return False
    return True


def dfs(cnt):
    if(cnt==N):
        global count1 
        count1 += 1
        return
    for i in range(N):
        chess[cnt] = i
        if condition(cnt):
            dfs(cnt+1)

dfs(0)
print(count1)

    


