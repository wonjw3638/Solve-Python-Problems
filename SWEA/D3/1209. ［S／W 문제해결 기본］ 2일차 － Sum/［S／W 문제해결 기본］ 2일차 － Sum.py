def my_max(a, b, c, d):
    tmp = a
    if tmp < b:
        tmp = b
    if tmp < c:
        tmp = c
    if tmp < d:
        tmp = d
    return tmp

for _ in range(1, 11):
    tc = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]

    max_row = max_col = 0  # 행, 열
    dig_l = dig_r = 0  # 좌, 우 대각선
    tmp_row = tmp_col = 0 # 임시 저장 값
    answer = 0  # 답

    for i in range(100):
        if max_row < tmp_row:
            max_row = tmp_row
        if max_col < tmp_col:
            max_col = tmp_col

        tmp_row = tmp_col = 0

        for j in range(100):
            tmp_row += numbers[i][j]
            tmp_col += numbers[j][i]

            if i == j :
                dig_l += numbers[i][j]
            if (i + j) == 99 :
                dig_r += numbers[i][j]
    
    print('#{} {}'.format(tc, my_max(max_row, max_col, dig_l, dig_r) ))