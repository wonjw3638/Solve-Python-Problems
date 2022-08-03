N = int(input())
first = N
num = 0

while (first != N or num == 0):
    a = N//10 + N%10
    N = (N%10)*10 + a%10
    num += 1

print(num)