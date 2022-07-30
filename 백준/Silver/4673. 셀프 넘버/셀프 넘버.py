list_a = [i for i in range(1,10000)]
list_c = []

def sum_a(i):      #본래 숫자 + 각자리 수 합을 구하는 함수정의
    n = len(str(i))
    r =[]
    for k in range(n):
        re = ((i%10**(k+1)) - (i%10**k))//(10**k)
        r.append(re)
    return sum(r)+i

for i in range(9999):
    s = sum_a(list_a[i])
    while True:
        if s not in list_c:
            list_c.append(s)
            s = sum_a(s)
        if s > 100 or s in list_c:
            break

l = len(list_c)

for i in range(l):
    if list_c[i] in list_a:
        list_a.remove(list_c[i])

l_a = len(list_a)

for i in range(l_a):
    print(list_a[i])