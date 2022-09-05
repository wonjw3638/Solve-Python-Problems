N = int(input())
a = N//5
answer = -1
while a > -1:
    if not ((N - (a * 5)) %  2) :
        answer = a + (N - (a * 5)) // 2
        break
    else:
        a -= 1

print(answer)