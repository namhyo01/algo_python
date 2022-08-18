

N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
def blackjack(card, N, M):
    max_blackjack = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                sum_card = card[i]+card[j]+card[k]
                if sum_card < max_blackjack:
                    continue
                elif sum_card == M:
                    return sum_card
                elif sum_card < M and sum_card>max_blackjack:
                    #print(i)
                    max_blackjack = sum_card
                else:
                    continue
    return max_blackjack

print(blackjack(card,N,M))