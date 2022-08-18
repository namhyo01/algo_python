def hanoi(n,a,b,c): # a: 출발 위치 c : 도착 위치 b : 깍두기 n = 원탑개수
    if n == 1:
        print(a,c)
        return
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
    
n = int(input())

print(2**n-1)
hanoi(n,1,2,3)