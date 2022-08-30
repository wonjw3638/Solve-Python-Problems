# 10026 적록색약

def dfs(map_list):
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                cnt += 1
                stack = list()
                v = [i, j]
                visited[i][j] = 1
                stack.append(v)

                while stack:
                    v = stack[-1]
                    c = map_list[v[0]][v[1]]

                    for d in range(4):
                        ni = v[0] + di[d]
                        nj = v[1] + dj[d]
                        if (0 <= ni < N) and (0 <= nj < N):
                            if visited[ni][nj] == 0:
                                if map_list[ni][nj] == c:
                                    visited[ni][nj] = 1
                                    stack.append([ni, nj])
                                    break
                    else:
                        stack.pop()

    return cnt

N = int(input())
color_map = list()
blindness_map = list()

for _ in range(N):
    color = input()
    color_map.append(color)
    blindness_map.append(color.replace('G', 'R'))

di = [0, -1, 0, 1]
dj = [1, 0, -1, 0]

answer1 = dfs(color_map)
answer2 = dfs(blindness_map)

print(answer1, answer2)