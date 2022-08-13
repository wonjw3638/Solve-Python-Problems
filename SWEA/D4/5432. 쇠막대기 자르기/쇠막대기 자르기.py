T = int(input())

for tc in range(1, T + 1):
    sticks = input()

    # 레이저인지, 쇠막대기인지 확인
    parenthesesOpen = False
    # 쇠막대기 개수
    count = 0
    answer = 0

    # 받은 input에 대한 for문
    for stick in sticks:
        # 입력값이 ( 인 경우
        if stick == '(':
            # 이 전에 ( 나왔었음
            if parenthesesOpen == True:
                count += 1
            else:
                parenthesesOpen = True
        # 입력값이 ) 인 경우
        else:
            # 해당 값이 레이저. 쇠막대 조각 += 1
            if parenthesesOpen == True:
                answer += count
                parenthesesOpen = False
            # 쇠막대 끝남 쇠막대 조각수 더하고 쇠막대기 개수 -= 1
            else:
                answer += 1
                count -= 1

    print('#{} {}'.format(tc, answer))