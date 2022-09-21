# 15650 N과 M 2
# 220921

# 조합 사용
def comb(arr, n):
    result = list()

    if n == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for j in comb(arr[i+1:], n-1):
            result.append([elem] + j)
    
    return result

N, M = list(map(int, input().split()))

# 1부터 N까지 배열
arr = [ i for i in range(1, N + 1)]

arrComb = comb(arr, M)

for answer in arrComb:
    print(*answer)