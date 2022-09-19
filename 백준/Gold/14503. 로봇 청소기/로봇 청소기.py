# 14503 로봇청소기
# 220916

import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**7)

# 왼쪽방향 0 1 2 3 
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

# 후진방향
bi = [1, 0, -1, 0]
bj = [0, -1, 0, 1]

def clean(i, j, d):
    global cnt

    visited[i][j] = 1
    for _ in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        
        if (0 <= ni < N) and (0 <= nj < M):
            # 방문하지 않은 곳, 벽 아님
            if (visited[ni][nj] == 0) and (arr[ni][nj] == 0):
                cnt += 1
                d = (d + 3)%4
                return clean(ni, nj, d)
        
        # 왼쪽으로 회전 (-1 이 곧 +3)
        d = (d + 3)%4

    # 4곳 다 방문 or 벽
    # 후진하기

    ni = i + bi[d]
    nj = j + bj[d]

    # 벽이 아니면 이동
    if (0 <= ni < N) and (0 <= nj < M):
        if arr[ni][nj] == 0:
            return clean(ni, nj, d)
        # 벽인 경우 
    return 


N, M = list(map(int, input().split()))
r, c, d = list(map(int, input().split()))
arr = [ list(map(int, input().split())) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
cnt = 1

clean(r, c, d)

print(cnt)