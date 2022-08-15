N = int(input())
serial = [input() for _ in range(N)]

# 숫자만 더하는 함수
numbers = [str(i) for i in range(10)]

def num_sum(string):
    total = 0
    for s in string:
        if s in numbers:
            total += int(s)
        else: continue
    return total

for i in range(N):
    min_idx = i
    for j in range(i+1, N):
        # 길이 짧은 거랑 자리 바꾸는 배열
        if len(serial[min_idx]) > len(serial[j]):
            min_idx = j
        # 숫자 합 비교, 작은 합 앞으로 바꾸는 배열
        elif len(serial[min_idx]) == len(serial[j]):
            if num_sum(serial[min_idx]) > num_sum(serial[j]):
                min_idx = j
            # 사전순 (숫자 - 알파벳)
            elif num_sum(serial[min_idx]) == num_sum(serial[j]):
                idx = 0
                while True:
                    if ord(serial[min_idx][idx]) > ord(serial[j][idx]):
                        min_idx = j
                        break
                    elif ord(serial[min_idx][idx]) == ord(serial[j][idx]):
                        idx += 1
                    else:
                        break
    serial[min_idx], serial[i] = serial[i], serial[min_idx]

for answer in serial:
    print(answer)