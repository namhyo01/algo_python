import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
plus,minus,mul,div = map(int, sys.stdin.readline().split())
max_num = -9999999999
min_num = 9999999999
def dfs(plus, minus, mul, div,cnt,result):
    global a
    if cnt == n:
        global max_num
        global min_num
        max_num = max(result, max_num)
        min_num = min(result, min_num)
    if plus>0:
        result = result + a[cnt]
        dfs(plus-1,minus,mul,div,cnt+1,result)
    if minus>0:
        result = result - a[cnt]
        dfs(plus,minus-1,mul,div,cnt+1,result)
    if mul>0:
        result = result * a[cnt]
        dfs(plus,minus,mul-1,div,cnt+1,result)
    if div>0:
        result = result / a[cnt]
        dfs(plus,minus,mul,div-1,cnt+1,result)

dfs(plus, minus, mul,div, 1,a[0])
print(max_num)
print(min_num)


