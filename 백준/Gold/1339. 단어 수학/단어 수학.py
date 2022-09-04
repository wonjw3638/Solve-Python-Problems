N = int(input())
alp = {}

for _ in range(N):
    string = input()
    idx = 1
    for s in string[::-1]:
        if s in alp:
            alp[s] += idx
        else:
            alp[s] = idx
        idx *= 10

alp = sorted(alp.items(), key = lambda items : items[1], reverse = True)
answer = 0
num = 9
for value in alp :
    answer += value[1] * num
    num -= 1

print(answer)