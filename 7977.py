n = int(input())
dna = input().strip()

aCnt = [dna.count('A'),'A']
cCnt = [dna.count('C'),'C']
gCnt = [dna.count('G'),'G']
tCnt = [dna.count('T'),'T']
ans = [aCnt,cCnt,gCnt,tCnt]
ans.sort()
print(ans[0][0])
print(ans[0][0]*n)
