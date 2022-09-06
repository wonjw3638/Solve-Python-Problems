C, R = list(map(int, input().split()))
N = int(input())
mapList = [[0] * C for _ in range(R)]

def check():
    if N > C * R:
        return [0]

    i = R
    j = 0
    direction = 0
    num = 1

    while num <= N:
        if direction == 0:
            if (0 <= i-1 < R) and (0 <= j < C):
                if mapList[i-1][j] != 0:
                    direction = (direction + 1) % 4
                    continue
                else:
                    mapList[i-1][j] = num
                    num += 1
                    i -= 1
                    continue
            else:
                direction = (direction + 1) % 4
                continue

        elif direction == 1:
            if (0 <= i < R) and (0 <= j+1 < C):
                if mapList[i][j+1] != 0:
                    direction = (direction + 1) % 4
                    continue
                else:
                    mapList[i][j+1] = num
                    num += 1
                    j += 1
                    continue
            else:
                direction = (direction + 1) % 4
                continue

        elif direction == 2:
            if (0 <= i+1 < R) and (0 <= j < C):
                if mapList[i+1][j] != 0:
                    direction = (direction + 1) % 4
                    continue
                else:
                    mapList[i+1][j] = num
                    num += 1
                    i += 1
                    continue
            else:
                direction = (direction + 1) % 4
                continue

        else:
            if (0 <= i <= R) and (0 <= j-1 <= C):
                if mapList[i][j-1] != 0:
                    direction = (direction + 1) % 4
                    continue
                else:
                    mapList[i][j-1] = num
                    num += 1
                    j -= 1
                    continue
            else:
                direction = (direction + 1) % 4
                continue

    return [j + 1, R - i]

answer = check()
print(*answer)