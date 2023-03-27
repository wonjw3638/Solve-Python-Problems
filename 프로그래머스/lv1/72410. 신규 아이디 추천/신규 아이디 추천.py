def solution(new_id):
    # 1단계
    new_id_1 = new_id.lower()
    # 2단계
    new_id_2 = ''
    for ch in new_id_1:
        ascii_num = ord(ch)
        if (48 <= ascii_num <= 57) or (ascii_num == 45) or (ascii_num == 46) or (ascii_num == 95) or (65 <= ascii_num <= 90) or (97 <= ascii_num <= 122):
            new_id_2 += ch
    
    # 3단계
    new_id_3 = ''
    stack = False
    for ch in new_id_2:
        if ch == '.':
            if stack:
                continue
            else:
                stack = True
                new_id_3 += ch
        else:
            stack = False
            new_id_3 += ch

    # 4단계
    new_id_4 = new_id_3
    if (len(new_id_3) > 0) and (new_id_3[0] == '.'):
        new_id_4 = new_id_3[1:]
        
    if (len(new_id_4) > 0) and (new_id_4[-1] == '.'):
        new_id_4 = new_id_4[:-1]
    
    # 5단계
    if not new_id_4:
        new_id_4 = 'a'
        
    # 6단계
    if len(new_id_4) >= 16:
        new_id_4 = new_id_4[:15]
        if new_id_4[14] == '.':
            new_id_4 = new_id_4[:14]
        
    # 7단계
    if len(new_id_4) <= 2:
        add = new_id_4[-1]
        while len(new_id_4) < 3:
            new_id_4 += add
            
    answer = new_id_4        
    
    return answer