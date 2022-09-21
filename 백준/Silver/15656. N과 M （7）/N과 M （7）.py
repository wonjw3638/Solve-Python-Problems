# 15656 N과 M 7
# 220921

# 중복순열 사용
def perm(arr, n):
    result = list()

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in perm(arr, n-1):
            result.append([elem] + j)
    
    return result

N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()

arrPerm = perm(arr, M)

for answer in arrPerm:
    print(*answer)