T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    doc_list = list(map(int, input().split()))

    cnt = 0

    while True:
        if M == 0 and max(doc_list) == doc_list[0]:
            cnt += 1
            break
        elif max(doc_list) == doc_list[0]:
            doc_list.pop(0)
            cnt += 1
            M -= 1
        else:
            doc_list.append(doc_list.pop(0))
            if M > 0:
                M -= 1
            else:
                M = len(doc_list) - 1
    
    print(cnt)
