num = [str(i) for i in range(10)]

for tc in range(1, 11):
    M = int(input())
    N = input()
    stack = [''] * M

    top = -1
    answer = ''

    # 수식 문자열 읽기
    for n in N:
        # 피연산자인 경우
        if n in num:
            answer += n
        # 연산자인 경우
        else:
            # stack이 비어있는 경우
            if top == -1:
                top = 0
                stack[top] = n
                continue
            else:
                while True:
                    if top == -1:
                        top = 0
                        stack[0] = n
                        break
                    else:
                        answer += stack[top]
                        stack[top] = ''
                        top -= 1

    for i in range(top, -1, -1):
        answer += stack[i]
        stack[i] = ''

    top = -1

    for a in answer:
        if a in num:
            top += 1
            stack[top] = int(a)
        else:
            tmp = stack[top] + stack[top-1]
            stack[top] = stack[top-1] = ''
            top -= 1
            stack[top] = tmp

    print('#{} {}'.format(tc, stack[0]))