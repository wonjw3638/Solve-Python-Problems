T = int(input())

for tc in range(1, T + 1):
    
    N, M = list(map(int, input().split()))
    arr = list()

    for _ in range(N):
        arr.append(list(map(int, input().split())))
    
    di = [0, 1]
    dj = [1, 0]

    answer = 0

    for i in range(N):
        for j in range(M):
            for d in range(2):
                if arr[i][j] == 1:
                    ti = i
                    tj = j
                    if (0 <= ti - di[d] < N) and (0 <= tj - dj[d] < M):
                        if arr[ti - di[d]][tj - dj[d]] == 0:
                            tmp = 1
                            while True:
                                if (0 <= ti + di[d] < N) and (0 <= tj + dj[d] < M):
                                    if arr[ti + di[d]][tj + dj[d]] == 1:
                                        tmp += 1
                                        ti += di[d]
                                        tj += dj[d]
                                    else:
                                        break
                                else: break
                        else: continue
                    else:
                        tmp = 1
                        while True:
                            if (0 <= ti + di[d] < N) and (0 <= tj + dj[d] < M):
                                if arr[ti + di[d]][tj + dj[d]] == 1:
                                    tmp += 1
                                    ti += di[d]
                                    tj += dj[d]
                                else:
                                    break
                            else: break
                    if tmp > answer:
                        answer = tmp
                else: continue

    print('#{} {}'.format(tc, answer))