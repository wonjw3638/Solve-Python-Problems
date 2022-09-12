import math
x, y, c = list(map(float, input().split()))

left, right = 0, min(x, y)

while (right - left) > 1e-6:
    mid = (left + right)/2
    d = mid
    tmp = ((math.sqrt((x**2) - (d**2))) * (math.sqrt((y**2) - (d**2))))/((math.sqrt((x**2) - (d**2))) + (math.sqrt((y**2) - (d**2))))
    if tmp < c:
        right = mid
    elif tmp > c:
        left = mid
    else:
        break

print('{:.3f}'.format(mid))