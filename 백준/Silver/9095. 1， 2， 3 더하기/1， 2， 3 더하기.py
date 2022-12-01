def find(n, string):
    if n == 0:
        if not string in answer:
            answer.append(string)
        return 
    
    for num in [1, 2, 3]:
        if n >= num:
            find(n-num, string + str(num))
        else:
            continue

T = int(input())
for _ in range(T):
    answer = list()
    N = int(input())

    find(N, '')

    print(len(answer))