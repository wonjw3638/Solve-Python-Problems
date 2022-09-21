# 14502 연구소
# 220920

import sys
input = sys.stdin.readline
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def comb(arr, n):
    result = list()

    if n == 0 :
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in comb(arr[i+1:], n-1):
            result.append([elem] +j)
    return result

def bfs(arr):
    queue = deque()
    for v in virus:
        visited[v[0]][v[1]] = 1
        queue.append(v)
    
    while queue:
        v = queue.popleft()
        i = v[0]
        j = v[1]
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < N and 0 <= nj < M :
                if (visited[ni][nj] == 0) and (arr[ni][nj] == 0):
                    visited[ni][nj] = visited[i][j] + 1
                    arr[ni][nj] = 2
                    queue.append([ni, nj])
    total = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                total += 1
    
    return total


N, M = list(map(int, input().split()))
lab = list()

# 연구소 0의 i, j 위치 받아놓기
makeWall = list()
virus = list()

for i in range(N):
    inputArr = list(map(int, input().split()))
    lab.append(inputArr)
    for j in range(M):
        if inputArr[j] == 0:
            makeWall.append([i, j])
        if inputArr[j] == 2:
            virus.append([i, j])

# 그 중에 3개 조합 사용해서 고르기
makeWall_comb = comb(makeWall, 3)
answer = 0

for makeWall3 in makeWall_comb:

    # 임시 배열 딥카피.
    lab_arr = [lab[i][:] for i in range(N)]
    for k in range(3):
        lab_arr[makeWall3[k][0]][makeWall3[k][1]] = 1
    # 바이러스 확산 - bfs 진행
    visited = [[0] * M for _ in range(N)]
    cnt = bfs(lab_arr)
    
    # 바이러스 갯수 세서 더 영역이 더 작으면 answer 값 update
    if answer < cnt:
        answer = cnt

print(answer)