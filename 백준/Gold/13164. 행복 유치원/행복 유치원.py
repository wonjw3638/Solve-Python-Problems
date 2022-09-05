N, K = list(map(int, input().split()))
kids = list(map(int, input().split()))

sub = list()
tmp = kids[0]
for kid in kids:
    sub.append(kid - tmp)
    tmp = kid

sub.sort(reverse=True)

answer = sum(sub[K-1:])
print(answer)