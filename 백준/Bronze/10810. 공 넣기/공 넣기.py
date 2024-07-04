N, M = map(int, input().split())

ball_list = ['0'] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i-1, j):
        ball_list[index] = str(k)


print(' '.join(ball_list))