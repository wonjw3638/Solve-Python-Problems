N, K = map(int, input().split())

countries = [0] * (N+1)
countries[0] = [0,0]

for _ in range(N):
    i, g, s, b = map(int, input().split())
    if i == K:
        score = 100*g + 10*s + b
    countries[i] = [100*g + 10*s + b, i]

countries.sort(key=lambda x: x[0], reverse=True)

for idx, country in enumerate(countries):
    if country[0] == score:
        print(idx+1)
        break
    if country[1] == K:
        print(idx+1)
        break