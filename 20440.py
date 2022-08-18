
import sys
from collections import defaultdict

input = sys.stdin.readline
check = defaultdict(int)
n = int(input())
time = list(tuple(map(int, input().split())) for _ in range(n))
time.sort(key=lambda x: (x[0],x[1])) 
for i in range(n):
    a,b = time[i]
    check[a]+=1
    check[b]-=1
hotTime = [0,0]
currcnt=0
nextCnt = 0
maxCnt = 0
firstFind = False
keysList = list(check.keys())
keysList.sort()
for i in keysList:
    nextCnt = currcnt + check[i]
    if nextCnt > maxCnt: # 갱신
        maxCnt= nextCnt
        firstFind = True
        hotTime[0] = i
    elif nextCnt == maxCnt and firstFind==True:
        hotTime[1] = i
    elif nextCnt < maxCnt and firstFind==True: # 즉 max가 더큰데 첫번쨰 찾은거라면 잘못찾음
        hotTime[1] = i
        firstFind = False
    currcnt = nextCnt

print(maxCnt)
print(hotTime[0],hotTime[1])
