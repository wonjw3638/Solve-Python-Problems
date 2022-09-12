from bisect import bisect_left

N = int(input())
numbers = list(map(int, input().split()))
Lis = list()
idx_list = list()

for i in numbers:
    k = bisect_left(Lis, i)
    idx_list.append(k)

    if len(Lis) <= k: 
        Lis.append(i)
    else:
        Lis[k] = i 
        
len_Lis = len(Lis)

print(len_Lis)

idx_list.reverse()
numbers.reverse()

answer = list()
len_Lis -= 1

for idx in range(N):
    if idx_list[idx] == len_Lis:
        answer.append(numbers[idx])
        len_Lis -= 1

answer.reverse()

print(*answer)