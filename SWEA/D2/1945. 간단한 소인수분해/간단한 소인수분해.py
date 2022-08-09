T = int(input())

for tc in range(1, T+1):

    N = int(input())
    answer = '#{}'.format(tc)
    quo = N
    for i in [2, 3, 5, 7, 11]:
        re, cnt = i, 0
        while True:
            if quo % i == 0: # 나누어 떨어지는 경우에 cnt += 1
                quo = quo//i
                cnt += 1
            else: 
                answer += (' ' + str(cnt))
                break

    print(answer)