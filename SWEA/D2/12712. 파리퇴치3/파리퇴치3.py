T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    fly = []
    for _ in range(N):
        fly.append(list(map(int, input().split()))) 
    
    di = [-1, 1, 0, 0, -1, -1, 1, 1]   # + 모양 / x 모양
    dj = [0, 0, -1, 1, -1, 1, -1, 1]   # 0~3, 4~7

    max_fly = 0
    for i in range(N):    # 노즐의 중심 
        for j in range(N):  
            for delta in [0, 4]: # 델타 0~3, 4~7
                fly_cnt = fly[i][j]
                for d in range(delta, 4 + delta): # 방향
                    for k in range(1,M):
                        if ((0 <= (i + (di[d] * k)) < N) and (0 <= (j + (dj[d] * k)) < N)):
                            fly_cnt += fly[i + (di[d] * k)][j + (dj[d] * k)]
                        else:
                            break
                if fly_cnt > max_fly:
                    max_fly = fly_cnt

    print('#{} {}'.format(tc, max_fly))