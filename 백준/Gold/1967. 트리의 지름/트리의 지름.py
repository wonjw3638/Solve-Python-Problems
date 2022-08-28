# 1967_트리의 지름
'''
설계 05:10 ~ 05:16
구현 05:17 ~ 
'''

N = int(input())
map_list = [[] for _ in range(N + 1)]

def dfs(s):
    visited = [0] * (N + 1)
    stack = [0] * (N + 1)
    top = -1
    v = s
    
    top += 1
    stack[top] = v
    visited[v] = 1

    while top >= 0:
        v = stack[top]
        for i, w in  map_list[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + w
                top += 1
                stack[top] = i
                break
        else:
            top -= 1
    return max(visited) - 1, visited.index(max(visited))

for _ in range(N - 1):
    a, b, w = list(map(int, input().split()))
    map_list[a].append([b, w])
    map_list[b].append([a, w])

# s 에서 시작
tmp, s = dfs(1)
answer, g = dfs(s)

print(answer)