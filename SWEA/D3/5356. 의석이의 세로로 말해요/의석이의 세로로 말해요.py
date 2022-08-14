T = int(input())

for tc in range(1, T + 1):
    string = [''] * 15
    for _ in range(5):
        input_string = input()
        for idx, s in enumerate(input_string):
            string[idx] += s

    answer = ''
    for ans in string:
        answer += ans

    print('#{} {}'.format(tc, answer))