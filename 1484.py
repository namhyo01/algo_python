G = int(input())

ans = []

left = 1
right = G
while(left<right):
    if(G%left==0): #나눠떨어지면
        right = int(G/left)
        x = (left+right)/2
        if(x==int(x)):
            ans.append(int(x))
    left+=1
    right = G/left

if(not ans):
    print(-1)
else:
    ans = list(set(ans))
    ans = sorted(ans,reverse=False)
    for i in ans:
        print(i)

