T = int(input())
for _ in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    num.sort()

    arr1 = num[0]
    arr2 = num[1]
    answer = 0
    idx = 2
    while idx + 1 < N:
        if answer < num[idx] - arr1:
            answer = num[idx] - arr1

        arr1 = num[idx]
        if answer < num[idx + 1] - arr2:
            answer = num[idx + 1] - arr2

        arr2 = num[idx + 1]
        idx += 2

    if answer < num[N-1] - arr1:
        answer = num[N-1] - arr1
    if answer < num[N-1] - arr2:
        answer = num[N-1] - arr2
    
    print(answer)