T = int(input())
pascal = [['1'], ['1',' ','1']]
pascal_table = 1

for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))

    for n in range(N):
        answer = []
        # 이미 계산해둔 값인 경우
        if n <= pascal_table:
            print(''.join(pascal[n]))
        # 아닌 경우
        else:
            answer.append('1')
            for i in range(0, ((2 * n) - 2),  2):
                answer.append(' ')
                answer.append('{}'.format(int(pascal[n - 1][i]) + int(pascal[n - 1][i + 2])))
            answer.extend([' ','1'])
            pascal.append(answer)
            pascal_table += 1
            print(''.join(answer))