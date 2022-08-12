T = int(input())

for _ in range(1, T + 1):
    tc, N = list(input().split())
    print(tc)
    str_list = list(input().split())
    str_count = [0] * 10
    string = {
        'ZRO' : 0,
        'ONE' : 1,
        'TWO' : 2,
        'THR' : 3,
        'FOR' : 4,
        'FIV' : 5,
        'SIX' : 6,
        'SVN' : 7,
        'EGT' : 8,
        'NIN' : 9,
    }

    for s in str_list:
        str_count[string.get(s)] += 1

    idx = 0
    for key in string.keys():
        for _ in range(str_count[idx]):
            print(key, end=' ')
        idx += 1
    print()