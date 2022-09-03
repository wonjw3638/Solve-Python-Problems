N = int(input())
K = int(input())

N_list = list(map(int, input().split()))
N_list.sort()

sub = list()
num = N_list[0]

for n in N_list[1:]:
    sub.append(n-num)
    num = n

sub.sort(reverse=True)
answer = sum(sub[K-1:])

print(answer)