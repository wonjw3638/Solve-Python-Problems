N = int(input())

answer = [-1] * N
temp = []

numbers = list(map(int,input().split()))

for idx, num in enumerate(numbers):
    while temp and (num > numbers[temp[-1]]):
        last = temp.pop()
        answer[last] = num
    temp.append(idx)

print(' '.join(list(map(str,answer))))