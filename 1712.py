A,B,C = map(int, input().split())

if (C<B): # 조건이 성립이안됌
    print(-1)
else:
    print(A//(C-B)+1)

    
    