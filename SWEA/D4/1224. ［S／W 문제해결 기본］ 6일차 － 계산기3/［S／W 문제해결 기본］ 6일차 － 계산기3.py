num = [str(i) for i in range(10)]
operator = {
    '(' : 0,
    '+' : 1, 
    '*' : 2, 
}

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
                top += 1
                stack[top] = n
                continue
            
            # 여는 괄호 연산자인 경우 push
            if n == '(':
                top += 1
                stack[top] = n
            else:
                if n == ')':
                    # 여는 괄호 연산자를 만날 때까지 pop
                    while True:
                        if stack[top] == '(':
                            stack[top] = ''
                            top -= 1
                            break
                        else:
                            answer += stack[top]
                            stack[top] = ''
                            top -= 1
                else:
                    while True:
                        # 스택이 비어있는 경우 종료.
                        if top == -1:
                            top += 1
                            stack[top] = n
                            break
                        # 더 낮은 연산자를 만날 때 까지 pop. 낮은 연산자를 만나면 push.
                        if operator.get(stack[top]) >= operator.get(n):
                            answer += stack[top]
                            stack[top] = ''
                            top -= 1
                        else:
                            top += 1
                            stack[top] = n
                            break

    for i in range(top, -1, -1):
        answer += stack[i]

    top = -1
    for a in answer:
        # 피연산자를 만나면 stack에 push
        if a in num:
            top += 1
            stack[top] = int(a)

        # 연산자를 만나면 위에 두개 연산, 연산 결과를 stack에 push
        else:
            if a == '+':
                tmp = stack[top] + stack[top-1]
                stack[top] = stack[top-1] = ''
                top -= 1
                stack[top] = tmp
            else:
                tmp = stack[top] * stack[top-1]
                stack[top] = stack[top-1] = ''
                top -= 1
                stack[top] = tmp
    
    print('#{} {}'.format(tc, stack[0]))