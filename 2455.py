import sys
max_people = 0
people = 0
for i in range(4):
    out, come = map(int,sys.stdin.readline().split())
    people -= out
    people += come
    max_people = max(max_people,people)
print(max_people)
    