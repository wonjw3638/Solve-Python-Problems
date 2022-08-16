# 회문 찾는 함수 만들기
def palindrome(string):
    max_length = 1
    # 행에서 찾기
    for s in string:
        # 회문의 길이 2~100, 1인 경우는 초기값은 1로 설정, 제외
        for M in range(2, 100):
            for k in range(101-M):
                answer = s[0 + k:M + k]
                # 회문인 경우
                if answer == answer[::-1]:
                    if M > max_length:
                        max_length = M
        
    # 열에서 찾기
    for j in range(100):
        for M in range(2, 100):
            for i in range(101 - M):
                answer = ''
                for k in range(M):
                    answer += string[i + k][j]
                if answer == answer[::-1]:
                    if M > max_length:
                        max_length = M
    
    return max_length


for _ in range(10):
    tc = int(input())
    string = [input() for _ in range(100)]
    answer = palindrome(string)

    print('#{} {}'.format(tc, answer))
