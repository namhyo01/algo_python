T = int(input())
for i in range(T):
    H,W,N = map(int, input().split())
    a = N/H
    a = str(int(a)) if a==int(a) else str(int(a)+1) #뒤 2자리
    a = a.zfill(2)
    B = N%H
    B = str(H) if B==0 else str(B)
    print(B+a)