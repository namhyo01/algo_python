import sys
input = sys.stdin.readline

def solve(n: int):
    if n==0 or n==1:
        return 1
    dp = [0 for _ in range(n+1)]
    dp[0]=1
    dp[1]=1
    # 한칸 배치는 세로타일 배치 하나 두칸 배치는 가로 타일 2개랑 2*2타일 배치 하는 방법 2개
    for i in range(2,n+1):
        dp[i] = dp[i-1]+2*dp[i-2]
    return dp[n]

while True:
    try:
        print(solve(int(input())))
    except:
        break
