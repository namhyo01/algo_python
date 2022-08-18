import sys
N = sys.stdin.readline()
N = sys.stdin.readline().replace('\n','')
result = 0
for i in N:
    result += int(i)

print(result)
