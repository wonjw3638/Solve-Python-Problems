def solution(answers):
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score1, score2, score3 = 0, 0, 0

    for idx, ans in enumerate(answers):
        if ans == std1[(idx%5)]: score1 += 1
        if ans == std2[(idx%8)]: score2 += 1
        if ans == std3[(idx%10)]: score3 += 1

    maxScore = max(score1, score2, score3)
    arr = [-1, score1, score2, score3]
    answer = []

    for idx, score in enumerate(arr):
        if score == maxScore:
            answer.append(idx)

    return answer