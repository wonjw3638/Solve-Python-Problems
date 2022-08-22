not_num = ['+', '-', '*', '/', '(', ')']
operator = {
    '(' : 0,
    '+' : 1, 
    '-' : 1, 
    '*' : 2, 
    '/' : 2, 
}

N = input()
stack = []
top = -1
answer = ''

# 수식 문자열 읽기
for n in N:
    # 피연산자인 경우
    if not (n in not_num):
        answer += n
    # 연산자인 경우
    else:
        # stack이 비어있는 경우
        if top == -1:
            stack.append(n)
            top += 1
            continue
        
        # 여는 괄호 연산자인 경우 push
        if n == '(':
            top += 1
            stack.append(n)

        else:
            if n == ')':
                # 여는 괄호 연산자를 만날 때까지 pop
                while True:
                    if stack[top] == '(':
                        stack.pop()
                        top -= 1
                        break
                    else:
                        answer += stack.pop()
                        top -= 1
            else:
                while True:
                    # 스택이 비어있는 경우 종료.
                    if top == -1:
                        top += 1
                        stack.append(n)
                        break
                    # 더 낮은 연산자를 만날 때 까지 pop. 낮은 연산자를 만나면 push.
                    if operator.get(stack[top]) >= operator.get(n):
                        answer += stack.pop()
                        top -= 1
                    else:
                        top += 1
                        stack.append(n)
                        break

for i in range(top, -1, -1):
    answer += stack[i]

print('{}'.format(answer))