num = [str(i) for i in range(10)]
operator = {
    '+' : 1, 
    '*' : 2, 
}

for tc in range(1, 11):
    M = int(input())
    N = input()
    stack = [''] * M
    # pop메소드 사용 안하기 위해서.. max_idx 값 따로 저장
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
            # 연산자가 + 일 때
            if n == '+':
                while True:
                    if top == -1:
                        top = 0
                        stack[0] = n
                        break
                    else:
                        answer += stack[top]
                        stack[top] = ''
                        top -= 1
            # 연산자가 x 일 때
            else:
                while True:
                    # 스택이 비어있는 경우 종료.
                    if top == -1:
                        top += 1
                        stack[top] = n
                        break

                    # 더 낮은 연산자를 만날 때 까지 pop
                    if stack[top] == '+':
                        top += 1
                        stack[top] = n
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