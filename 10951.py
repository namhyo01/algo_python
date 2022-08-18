import sys
import sys
count = 0
while True:
    try:
        A,B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break
    