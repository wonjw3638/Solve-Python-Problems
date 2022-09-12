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

numbers_reverse = numbers[::-1]
num_dp_reverse = [1] * N
dp_reverse = [ [numbers_reverse[i]] for i in range(N) ]

for i in range(1, N):
    for j in range(i):
        if numbers_reverse[i] > numbers_reverse[j]:
            if len(dp_reverse[i]) > len(dp_reverse[j]) + 1 :
                dp_reverse[i] = dp_reverse[i]
            else:
                dp_reverse[i] = dp_reverse[j] + [numbers_reverse[i]]
                num_dp_reverse[i] = num_dp_reverse[j] + 1

num_dp_reverse = num_dp_reverse[::-1]
max_len = [-1] * N

for i in range(N):
    max_len[i] = num_dp[i] + num_dp_reverse[i] - 1

print(max(max_len))