# 11052 카드 구매하기

N = int(input())
card = [0]
card += list(map(int, input().split()))

# 카드 n개를 가장 비싸게 사는 경우
dp = [0] * (N + 1)

# 짐 용량 - 카드 개수 - card index
# 짐의 가치 - 카드 가격 - card

for n in range(1, N + 1):
    # 고려하는 카드 수
    q = 0
    for i in range(n):
        q = max(q, dp[i] + card[n-i])
    dp[n] = q

print(dp[n])