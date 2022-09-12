N = int(input())
numbers = list(map(int, input().split()))
num_dp = [1] * N
dp = [ [numbers[i]] for i in range(N) ]

for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            if len(dp[i]) > len(dp[j]) + 1 :
                dp[i] = dp[i]
            else:
                dp[i] = dp[j] + [numbers[i]]
                num_dp[i] = num_dp[j] + 1

max_idx = max(num_dp)
idx = num_dp.index(max_idx)
print(max_idx)
print(*dp[idx])