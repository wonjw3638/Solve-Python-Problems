for tc in range(1, 11):
    N = int(input())
    magnetic = list()
    for _ in range(100):
        magnetic.append(list(input().split()))

    answer = 0
    for j in range(100):
        tmp = ''
        len_tmp = 0
        # 열의 값을 문자열로 0을 제외하고 받음
        for i in range(100):
            if magnetic[i][j] != '0':
                tmp += magnetic[i][j]
                len_tmp += 1
        # tmp에서 '12'의 개수 찾기
        for idx in range(len_tmp - 1):
            if tmp[idx] == '1':
                if tmp[idx + 1] == '2':
                    answer += 1
            else: continue

    print('#{} {}'.format(tc, answer))