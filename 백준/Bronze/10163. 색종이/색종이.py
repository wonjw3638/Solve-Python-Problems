import sys
input = sys.stdin.readline

N = int(input())

map_list = [[0] * 1001 for _ in range(1001)]

if N == 1:
    x, y, w, h = list(map(int, input().split()))
    print(w * h)

else:
    paper = list()
    answer = list()

    for _ in range(N):
        paper.append(list(map(int, input().split())))
    
    for idx in range(N-1, -1, -1):
        x, y, w, h = paper[idx]
        tmp = 0
        for j in range(w):
            for i in range(h):
                if map_list[y+i][x+j] > 0:
                    continue
                else:
                    map_list[y+i][x+j] = 1
                    tmp += 1
        answer.append(tmp)
    
    for idx in range(N-1, -1, -1):
        print(answer[idx])