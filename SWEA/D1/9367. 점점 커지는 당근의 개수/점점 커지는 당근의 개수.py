T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split())) + [0]   # 마지막에 끝나는 경우 체크를 위해 추가해줌
    C = 11  # 범위를 벗어난 큰 값
    maxCount = cnt = 0
    for carrot in carrots:
        if carrot <= C: # count 초기화
            if cnt > maxCount:
                maxCount = cnt
            C = carrot
            cnt = 1
        else: # 당근 크기가 커진 경우
            C = carrot
            cnt += 1
    
    print('#{} {}'.format(tc, maxCount))