import string
S = input()
alphabet = list(string.ascii_lowercase)
S = [i for i in S]
for i in range(26):
    try:
        print(S.index(alphabet[i]), end=' ')
    except:
        print(-1, end =' ')
