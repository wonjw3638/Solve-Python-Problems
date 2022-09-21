# 15654 N과 M 5
# 220921

# 순열 사용
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
arr = list(map(int, input().split()))
arr.sort()

arrPerm = perm(arr, M)

for answer in arrPerm:
    print(*answer)