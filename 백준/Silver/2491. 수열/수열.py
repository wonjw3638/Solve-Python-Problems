N = int(input())
arr = list(map(int, input().split()))

answer = cnt = 0

tmp = arr[0]
for num in arr:
    if num - tmp >= 0:
        cnt += 1
        tmp = num
    else:
        if cnt > answer:
            answer = cnt
        cnt = 1
        tmp = num
if cnt > answer:
    answer = cnt

cnt = 0
tmp = arr[-1]
for num in arr[::-1]:
    if num - tmp >= 0:
        cnt += 1
        tmp = num
    else:
        if cnt > answer:
            answer = cnt
        cnt = 1
        tmp = num
if cnt > answer:
    answer = cnt

print(answer)