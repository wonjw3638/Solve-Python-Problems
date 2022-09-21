# 15652 N과 M 4
# 220921

# 중복순열 사용
def perm(arr, n):
    result = list()

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in perm(arr[i:], n-1):
            result.append([elem] + j)
    
    return result

N, M = list(map(int, input().split()))

# 1부터 N까지 배열
arr = [ i for i in range(1, N + 1)]

arrPerm = perm(arr, M)

for answer in arrPerm:
    print(*answer)