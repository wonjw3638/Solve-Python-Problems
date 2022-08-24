for _ in range(10):
    front = 0
    rear = 7

    tc = int(input())
    queue = list(map(int, input().split()))
    chk = False

    while True:
        if chk == True: 
            break
        for k in range(1,6):
            tmp = queue[front] - k
            if tmp <= 0:
                tmp = 0
                chk = True
            for idx in range(1, rear + 1):
                queue[idx-1] = queue[idx]
            queue[rear] = tmp
            if chk == True:
                break
            else:
                continue

    answer = ''
    for q in queue:
        answer += (str(q) + ' ')

    print('#{} {}'.format(tc, answer))