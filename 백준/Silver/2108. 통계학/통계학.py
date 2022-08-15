# 통계학
# 시간초과

N = int(input())
num_list = list()

for _ in range(N):
    num_list.append(int(input()))

# 정렬
num_list.sort()

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

print(num_list[N//2])

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

print(max(num_list) - min(num_list))