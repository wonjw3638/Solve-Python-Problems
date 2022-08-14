T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = list()
    for _ in range(N):
        matrix.append(list(input().split()))
    
    answer = [[''] for _ in range(N)]

    # 90도 회전
    for i in range(N):
        for j in range(N):
            answer[i] += matrix[N-1-j][i]
        answer[i] += ' '

    # 180도 회전
    for i in range(N):
        for j in range(N):
            answer[i] += matrix[N-1-i][N-1-j]
        answer[i] += ' '

    # 270도 회전
    for i in range(N):
        for j in range(N):
            answer[i] += matrix[j][N-1-i]

    print('#{}'.format(tc))
    for ans in answer:
        print('{}'.format(''.join(ans)))