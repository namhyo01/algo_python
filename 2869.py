A,B,V = map(int, input().split())
k = (V-B)/(A-B)
k = k if k==int(k) else int(k)+1
print(int(k))