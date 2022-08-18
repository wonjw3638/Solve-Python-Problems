for tc in range(1, 11):
    N, string = list(input().split())
    stack = [-1] * int(N)
    stack[0] = string[0]
    top = 0
    for s in string[1:]:
        # stack 마지막 값과 같은 경우
        if stack[top] == s:
            stack[top] = -1
            top -= 1
        # stack 마지막 값과 다른 경우
        else:
            top += 1
            stack[top] = s

    answer = ''
    for s in stack:
        if s != -1:
            answer += s

    print('#{} {}'.format(tc, answer))