T = int(input())

# 우하좌상 순으로 
di = [0, +1, 0, -1]
dj = [+1, 0, -1, 0]

for tc in range(1, T+1):
    N = int(input())
    num_list = [[0] * N for _ in range(N)]
    value = 1
    ni = nj = 0
    for n in range(N, 0, -2):
        for d in range(4):
            while (0 <= ni < N) and (0 <= nj < N):
                num_list[ni][nj] = value
                if not ((0 <= ni+di[d] < N) and (0 <= nj+dj[d] < N)):
                    break
                if num_list[ni + di[d]][nj + dj[d]] != 0:
                    break
                value += 1
                ni += di[d]
                nj += dj[d]

    print('#{}'.format(tc))
    for li in num_list:
        print(' '.join(list(map(str,li))))