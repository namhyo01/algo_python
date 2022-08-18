import sys

n = int(sys.stdin.readline())
word = []
for i in range(n):
    word.append(sys.stdin.readline())
word = list(set(word)) # 중복제거
new_word = []
for i in word:
    new_word.append((len(i),i.replace('\n','')))
word = sorted(new_word)
for num, w in word:
    print(w)

