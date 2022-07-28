def solution(id_list, report, k):
    
    answer = [0] * len(id_list)
    block = {x : 0 for x in id_list}
    
    for i in set(report):
        block[i.split()[1]] += 1
    
    for i in set(report):
        if block[i.split()[1]] >= k:
            answer[id_list.index(i.split()[0])] += 1

    return answer