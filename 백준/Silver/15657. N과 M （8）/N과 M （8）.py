# 15657 N과 M 8
# 220921

# 중복 조합 사용
def comb(arr, n):
    result = list()

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in comb(arr[i:], n-1):
            result.append([elem] + j)
    
    return result

N, M = list(map(int, input().split()))

arr = list(map(int, input().split()))
arr.sort()

arrComb = comb(arr, M)

for answer in arrComb:
    print(*answer)