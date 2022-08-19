import sys
# 시간복잡도는 NlogK
# A배열을 만드는것은 10^10의 시간복잡도이므로 out...
# 실마리를 찾는 도중 좋은 팁을 얻었다 저것을 만들지 말자
# -i행 기준 m보다 작은 개수는 i*f 에서f수이다
# 즉 5행에서 25보다 작은 개수는 5개(25/5) 4행에서는 6개(25/4)가 된다
# 거시서 N행을 도입해 6보다 큰 경우를 대비한다
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
l,h = 0,K
ans = 0
while l<=h:
    mid = (l+h)//2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(mid//i,N)
    if cnt<K:
        l = mid+1
    else:
        ans,h = mid,mid-1

print(ans)