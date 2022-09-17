import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(M):
        tmp = list()
        if (0 <= i + 3 < N):
            tmp.append(sum(arr[i+k][j]  for k in range(4)))

        if (0 <= j + 3 < M):
            tmp.append(sum(arr[i][j:j+4]))

        if (0 <= i + 1 < N) and (0 <= j + 1 < M):
            tmp.append(sum(arr[i][j:j+2]) + sum(arr[i+1][j:j+2]))

        if (0 <= i + 2 < N) and (0 <= j + 1 < M):
            tmp.append(sum(arr[i+k][j] for k in range(3)) + arr[i+2][j+1])
            tmp.append(sum(arr[i+k][j+1] for k in range(3)) + arr[i+2][j])
            tmp.append(sum(arr[i+k][j]  for k in range(3)) + arr[i][j+1])
            tmp.append(sum(arr[i+k][j+1]  for k in range(3)) + arr[i][j])
            tmp.append(sum(arr[i+k][j+1]  for k in range(3)) + arr[i+1][j])
            tmp.append(sum(arr[i+k][j] for k in range(3)) + arr[i+1][j+1])
            tmp.append(sum(arr[i+k][j] for k in range(2)) + sum(arr[i+k][j+1] for k in range(1,3)))
            tmp.append(sum(arr[i+k][j] for k in range(1,3)) + sum(arr[i+k][j+1] for k in range(2)))

        if (0 <= i + 1 < N) and (0 <= j + 2 < M):
            tmp.append(sum(arr[i+1][j:j+3]) + arr[i][j+2])
            tmp.append(sum(arr[i+1][j:j+3]) + arr[i][j])
            tmp.append(sum(arr[i][j:j+3]) + arr[i+1][j])
            tmp.append(sum(arr[i][j:j+3]) + arr[i+1][j+2])
            tmp.append(sum(arr[i][j:j+3]) + arr[i+1][j+1])
            tmp.append(sum(arr[i+1][j:j+3]) + arr[i][j+1])
            tmp.append(sum(arr[i+1][j:j+2]) + sum(arr[i][j+1:j+3]))
            tmp.append(sum(arr[i][j:j+2]) + sum(arr[i+1][j+1:j+3]))
        
        if tmp:
            if answer < max(tmp):
                answer = max(tmp)

print(answer)