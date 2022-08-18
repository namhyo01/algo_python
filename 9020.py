import math
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i==0:
            return False
    return True

T = int(input())
for i in range(T):
    n = int(input())
    minus = 9999999
    num1 = 0
    num2 = 0
    for n1 in range(2,n//2+1):
        if isPrime(n1):
            if isPrime(n-n1):
                n2 = n-n1
                if min(minus, n2-n1) == (n2-n1):
                    minus = min(minus, n2-n1)
                    num1,num2 = n1,n2

    print(num1, end=' ')
    print(num2)
