T = int(input())

for tc in range(1, T + 1):
    # 1일 1달 3달 1년
    fee = list(map(int, input().split()))
    month = list(map(int, input().split()))

    # 월별 싼 요금 값
    min_month = [0] * 15
    # index월 까지 최적의 요금 값
    acc_min_val = [0] * 15

    # m월에 대한 최적의 요금 찾기
    for m in range(1, 13):
        # 1일권, 1달권 사용값 비교, min_month에 업데이트
        minVal = min(month[m-1] * fee[0] , fee[1])
        min_month[m] = minVal
        acc_min_val[m] = acc_min_val[m-1] + minVal

    # 3달권 사용할때 값 비교
    for m in range(3, 15):
        q = min(acc_min_val[m-3] + fee[2], acc_min_val[m-1] + min_month[m] )
        acc_min_val[m] = q

    # 1년권 비교
    answer = min(fee[3], acc_min_val[12])

    print('#{} {}'.format(tc, answer))