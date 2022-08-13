T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))

    max_val = answer = 0

    # 뒤에서부터 최댓값이 나올 때 까지 탐색, 차액 더해줌
    for i in price[::-1]:
        if i > max_val:
            max_val = i
        else:
            answer += (max_val - i)

    print('#{} {}'.format(tc, answer))