# 2579 계단 오르기

N = int(input())

stair = [0]

for _ in range(N):
    stair.append(int(input()))

def step(N):
    if N == 1:
        return stair[1]
    if N == 2:
        return stair[1] + stair[2]
    ## idx번째 계단까지 최대값
    dp_list[1] = stair[1]
    dp_list[2] = stair[2] + stair[1]

    for idx in range(3, N + 1):
        dp_list[idx] = max(dp_list[idx - 2] + stair[idx], dp_list[idx-3] + stair[idx - 1] + stair[idx])
    
    return dp_list[N]

dp_list = [0] * (N + 1)

answer = step(N)
print(answer)