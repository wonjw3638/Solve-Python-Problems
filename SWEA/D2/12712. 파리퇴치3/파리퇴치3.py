T = int(input())

di = [-1, 0, 1, 0, -1, -1, 1, 1]
dj = [0, 1, 0, -1, -1, 1, 1, -1]

for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    map_list = list()

    for _ in range(N):
        map_list.append(list(map(int, input().split())))
    
    answer = 0

    for i in range(N):
        for j in range(N):
            for d in [0, 4]:
                tmp = map_list[i][j]
                for dij in range(4):
                    for m in range(1, M):
                        if (0 <= i + (m * di[d + dij]) < N) and (0 <= j + (m * dj[d + dij]) < N):
                            tmp += map_list[i + (m * di[d + dij])][j + (m * dj[d + dij])]
                        else:
                            break
                if tmp > answer:
                    answer = tmp
    
    print('#{} {}'.format(tc, answer))