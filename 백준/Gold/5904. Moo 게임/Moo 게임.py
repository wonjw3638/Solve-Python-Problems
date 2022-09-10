N = int(input())
n = tmp = 3

while True:
    if tmp >= N:
        break
    else:
        n += 1
        tmp = 2 * tmp + n

moo = 'moo'

while True:
    if tmp <= 3:
        print(moo[N-1])        
        break
    if N <= (tmp - n) // 2 :
        tmp = (tmp - n) // 2
        n -= 1
    elif (tmp - n) // 2 < N <= ((tmp - n) // 2) + n:
        N -= (tmp - n) // 2
        moo = 'm' + ('o' * (n - 1))
        print(moo[N-1]) 
        break
    else:
        N -= ((tmp - n) // 2) + n
        tmp = (tmp - n) // 2
        n -= 1