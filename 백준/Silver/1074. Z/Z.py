N, r, c = list(map(int, input().split()))

def search(i, j, N, num):
    if N == 1:
        if r == i:
            if c == j:
                return num
            else:
                return num + 1
        else:
            if c == j:
                return num + 2
            else:
                return num + 3
    N -= 1
    if i <= r < i + 2**N:
        if j <= c < j + 2**N:
            return search(i, j, N, num)
        else:
            return search(i, j + (2**N), N, num + ((2**N)**2))
    else:
        if j <= c < j + 2**N:
            return search(i + (2**N), j, N, num + (2 * ((2**N)**2)))
        else:
            return search(i + (2**N), j + (2**N), N, num + (3 * ((2**N)**2)))

answer = search(0, 0, N, 0)
print(answer)