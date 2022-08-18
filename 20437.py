from collections import defaultdict
import sys
# a = sys.stdin.readline


T = int(sys.stdin.readline())
for _ in range(T):
    W = list(map(lambda x: ord(x)-97, sys.stdin.readline().strip()))
    K = int(sys.stdin.readline())
    
    alphabet = [[] for _ in range(26)]
    for idx,val in enumerate(W):
        alphabet[val].append(idx)
    smallest = 1000000
    largest = -1
    for a in alphabet:
        for i in range(len(a)-K+1):
            temp = a[i+K-1]-a[i] + 1
            smallest = min(smallest, temp)
            largest = max(largest,temp)
    if(largest==-1):
        print(-1)
    else:
        print(smallest, largest)

    # for i in range(len(W)):
    #     if(W.count(W[i])>=K):
    #         alphabet[W[i]].append(i)
    # if not alphabet:
    #     print(-1)
    #     continue
    # smallest = 1000000
    # largest = 0

    # for i in alphabet.values():
    #     for j in range(len(i)-K+1):
    #         temp = i[j+K-1] - i[j] + 1
    #         smallest = smallest if smallest<temp else temp
    #         largest = largest if largest>temp else temp
    # print(smallest, largest)

