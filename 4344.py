C = int(input())
for i in range(C):
    N_Score = list(map(int, input().split()))
    del N_Score[0]
    avg_score = sum(N_Score) / len(N_Score)
    cnt = 0
    for i in N_Score:
        if i > avg_score:
            cnt = cnt+1
    print("{:.3f}%".format((cnt/len(N_Score))*100))