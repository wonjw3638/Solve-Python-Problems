from bisect import bisect_left

N = int(input())
numbers = list(map(int, input().split()))
numbers = numbers[::-1]
Lis = list()

for i in numbers:
    k = bisect_left(Lis, i) 

    if len(Lis) <= k: 
        Lis.append(i)
    else:
        Lis[k] = i 
        
print(len(Lis))