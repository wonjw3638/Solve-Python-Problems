# 15649 N과 M 1
# 220921


def perm(arr, n):
    result = list()

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in perm(arr[:i] + arr[i+1:], n-1):
            result.append([elem] + j)
    
    return result

N, M = list(map(int, input().split()))

arr = [ i for i in range(1, N + 1)]

arrPerm = perm(arr, M)

for answer in arrPerm:
    print(*answer)