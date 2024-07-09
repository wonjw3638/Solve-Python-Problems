P = int(input())

for tc in range(P):
    students = list(map(int, input().split()))[1:]

    talls = []
    maxTall = 0
    total = 0

    for cnt, student in enumerate(students):
        if maxTall == 0:
            talls.append(student)
            maxTall = student
            continue

        if student > maxTall:

            talls.append(student)
            maxTall = student
            continue
        else:

            for idx, tall in enumerate(talls):
                if student < tall:
                    total += len(talls) - idx
                    talls = talls[:idx] + [student] + talls[idx:]
                    break
    
    print(tc+1, total)