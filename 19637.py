import sys
from bisect import *

N,M = map(int,sys.stdin.readline().split())
title, value = [],[]
for _ in range(N):
    t,v = sys.stdin.readline().split()
    title.append(t)
    value.append(int(v))

for _ in range(M):
    power = int(sys.stdin.readline())
    print(title[bisect_left(value,power)])



















