import itertools

a = list(map(int, input().split()))
N , S = a
numbers = list(map(int, input().split()))
cnt = 0

for i in range(1, len(numbers)+1):
    for a in itertools.combinations(numbers,i):
        if sum(a) == S:
            cnt += 1

print(cnt)