T = int(input())

for tc in range(1, T + 1):
    A, B = list(input().split())

    idx = cnt = answer = lenB = lenA = 0

    for b in B:
        lenB += 1
    for a in A:
        lenA += 1

    for i in range(lenA):
        if A[i] == B[idx]:
            if idx == (lenB - 1):
                idx = 0
                cnt += 1
            else:
                idx += 1
        else:
            if A[i] == B[0]:
                idx = 1
            else:
                idx = 0
    answer = lenA - ( cnt * (lenB - 1) )

    print('#{} {}'.format(tc, answer))
