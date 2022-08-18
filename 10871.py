import sys

N,X = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
A = [a for a in A if a<X]
for i in A:
    print(i, end =' ')