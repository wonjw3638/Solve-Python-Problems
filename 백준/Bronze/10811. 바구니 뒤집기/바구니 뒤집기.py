N, M = map(int, input().split())

basket = [str(i) for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    temp_list = basket[i-1:j][::-1]
    basket[i-1:j] = temp_list

print(' '.join(basket))