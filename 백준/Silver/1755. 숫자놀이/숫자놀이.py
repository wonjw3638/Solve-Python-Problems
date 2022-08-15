M, N = list(map(int, input().split()))

eng = {
    0 : 'zero',   
    1 : 'one',   
    2 : 'two',   
    3 : 'three',   
    4 : 'four',   
    5 : 'five',   
    6 : 'six',   
    7 : 'seven',   
    8 : 'eight',   
    9 : 'nine',   
}

eng_list = list()

for num in range(M, N+1):
    if num > 9:
        eng_list.append('{}{}'.format(eng.get(num // 10), eng.get(num % 10)))
    else:
        eng_list.append(eng.get(num))

eng_list.sort()
answer = ' '.join(eng_list)
for key, value in eng.items():
    answer = answer.replace(value, str(key))

cnt = 0
for ans in answer:
    if cnt == 10:
        print()
        cnt = 0
    if ans == ' ':
        cnt += 1
    print(ans, end = '')