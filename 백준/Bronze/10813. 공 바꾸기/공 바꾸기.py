N, M = map(int, input().split())

ball_list = [ str(i) for i in range(1, N+1) ]

for _ in range(M):
    i, j = map(int, input().split())
    ball_list[i-1], ball_list[j-1] = ball_list[j-1], ball_list[i-1]

print(' '.join(ball_list))