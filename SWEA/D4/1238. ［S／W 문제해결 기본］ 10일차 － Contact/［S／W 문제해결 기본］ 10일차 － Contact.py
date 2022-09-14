from collections import deque

for tc in range(1, 11):
    tel = [[] for _ in range(101) ]
    visited = [0] * 101
    N, start = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    # 트리구조 저장
    for i in range(0, N, 2):
        if arr[i+1] in tel[arr[i]]:
            pass
        else:
            tel[arr[i]].append(arr[i+1])

    # bfs
    queue = deque()
    queue.append(start)
    visited[start] += 1

    while queue:
        v = queue.popleft()
        for w in tel[v]:
            if not visited[w]:
                visited[w] = visited[v] + 1
                queue.append(w)
            else:
                continue
    
    max_visited = max(visited)

    for i in range(100, -1, -1):
        if visited[i] == max_visited:
            answer = i
            break

    print('#{} {}'.format(tc, answer))