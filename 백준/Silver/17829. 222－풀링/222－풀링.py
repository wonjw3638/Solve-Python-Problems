import sys
input = sys.stdin.readline

N = int(input())
map_list = list()
for _ in range(N):
    map_list.append(list(map(int, input().split())))

while N > 1:
    tmp_list = [[0] * (N // 2) for _ in range(N//2)]

    for i in range(0, N, 2):
        for j in range(0, N, 2):
            tmp = list()
            for di in range(2):
                for dj in range(2):
                    tmp.append(map_list[i + di][j + dj])
            tmp.sort(reverse=True)
            tmp_list[i//2][j//2] = tmp[1]
    
    N = N // 2
    if N == 1:
        answer = tmp_list[0]
        break
    else:
        map_list = [tmp_list[i] for i in range(N)]

print(answer[0])