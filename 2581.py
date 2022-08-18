import math
def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i==0:
            return False
    return True
M = int(input())
N = int(input())
Prime = []
for i in range(M,N+1):
    if isPrime(i):
        Prime.append(i)
if len(Prime) !=0:
    print(sum(Prime))
    print(min(Prime))
else:
    print(-1)
    
    

