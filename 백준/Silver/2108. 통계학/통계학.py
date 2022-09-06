# 2108_통계학

N = int(input())
num_list = list()

for _ in range(N):
    num_list.append(int(input()))

# 정렬
num_list.sort()

# 산술평균
check = False
avg = sum(num_list)/N

if avg < 0:
    print(int(round(avg)))
else:
    for s in str(avg):
        if s == '.':
            check = True
            continue
        if check == True:
            if int(s) >= 5:
                print(sum(num_list)//N + 1)
                break
            else:
                print(sum(num_list)//N)
                break

# 중앙값
print(num_list[N//2])

# 최빈값
# 중복제거
num_set = set(num_list)

count = { num : 0 for num in num_set}
for n in num_list:
    count[n] += 1

max_count = list()
max_val = max(count.values())
for key, val in count.items():
    if val == max_val:
        max_count.append(key)

max_count.sort()
if len(max_count) > 1:
    print(max_count[1])
else:
    print(max_count[0])

# 범위
print(max(num_list) - min(num_list))