A, B, C = list(map(int, input().split()))

def f(a, b):
    if b == 1:
        return a % C

    else:
        tmp = f(a, b // 2)

        # b가 짝수인 경우
        if b % 2 == 0:
            return (tmp * tmp) % C

        # b가 홀수인 경우
        else:
            return (tmp * tmp * a) % C

print(f(A,B))