while(True):
    n,k = map(int, input().split())
    if n==0 and k==0:
        break
    
    kk = n-k if k>n-k else k
    nprime = 1
    kprime = 1
    for i in range(kk):
        nprime *= (n-i)
    for j in range(1,kk+1):
        kprime *= j
    print(int(nprime/kprime))
