num = list(map(int, input().split()))
answer = list()

for idx, n in enumerate([1, 1, 2, 2, 2, 8]):
    answer.append(n - num[idx])

print(*answer)