T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if numbers[minIdx] > numbers[j]:
                minIdx = j
        numbers[i], numbers[minIdx] = numbers[minIdx] , numbers[i]
    
    print('#{}'.format(tc), *numbers)