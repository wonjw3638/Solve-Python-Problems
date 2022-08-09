T = int(input())

for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))
    boxes = [0] * (N + 1)
    idx = 1
    for q in range(Q):
        L, R = list(map(int, input().split()))
        for i in range(L, R+1):
            boxes[i] = idx
        idx += 1
    
    answer = '#{}'.format(tc)
    for b in boxes[1:]:
        answer += (' ' + str(b))

    print(answer)