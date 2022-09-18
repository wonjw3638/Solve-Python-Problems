# 15686 치킨배달
# 220916

def combi(arr, N):
    result = list()

    if N == 0:
        return [[]]
    else:
        for i in range(len(arr)):
            elem = [arr[i]]
            for j in combi(arr[i+1:], N-1):
                result.append(elem + j)
    return result

N, M = list(map(int, input().split()))
arr = list()
chicken_list = list()
home_list = list()

for i in range(N):
    arr_input = list(map(int, input().split()))
    for j in range(N):
        if arr_input[j] == 2:
            chicken_list.append([i, j])
        if arr_input[j] == 1:
            home_list.append([i, j])
    arr.append(arr_input)

chicken_combi = combi(chicken_list, M)

answer = 987654312

for chickens in chicken_combi:

    chicken_sum = 0
    for home in home_list:
        tmp = 987654312
        hi, hj = home
        for chicken in chickens:
            ci, cj = chicken
            d = abs(hi-ci) + abs(hj-cj)
            if d < tmp:
                tmp = d
        chicken_sum += tmp
    if chicken_sum < answer:
        answer = chicken_sum
        

print(answer)