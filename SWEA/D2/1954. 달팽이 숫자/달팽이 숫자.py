T = int(input())

def snail(N):
    i = j = d = 0
    num = 1
    arr[i][j] = num

    if N == 1:
        return 

    while num < (N**2):
        if 0 <= i + di[d] < N and 0 <= j + dj[d] < N:
            # 이미 채운 칸인 경우
            if arr[i + di[d]][j + dj[d]] != 0:
                d = ((d + 1) % 4 )
                continue
            else:
                i += di[d]
                j += dj[d]
                num += 1
                arr[i][j] = num
        # 범위 벗어 나는 경우
        else:
            d = ((d + 1) % 4 )
            continue

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    snail(N)
 
    print('#{}'.format(tc))
    for ar in arr:
        print(*ar)