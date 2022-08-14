N = int(input())

num_list = list()
for _ in range(N):
    num_list.append(int(input()))

for n in range(N):
    minIdx = n
    for i in range(n+1, N):
        if num_list[i] < num_list[minIdx]:
            minIdx = i
    num_list[n], num_list[minIdx] = num_list[minIdx], num_list[n]

for num in num_list:
    print(num)