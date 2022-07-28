def solution(places):
    answer = []
    for i in places:
        x, y = 0, 0
        if check(i, x, y) == True : answer.append(1)
        else: answer.append(0)
    return answer

def check(place, x, y):
    for i in place:
        y = 0
        for j in i:
            if j == "P":
                for a, b in [0,1], [1,0], [0,-1],[-1,0]:
                    if x+a<0 or x+a>4 or y+b<0 or y+b>4: continue
                    if place[x+a][y+b] == "P":
                        return False
                for a, b, c, d in [0,2,0,1], [0,-2,0,-1], [2,0,1,0], [-2,0,-1,0]:
                    if x+a<0 or x+a>4 or y+b<0 or y+b>4: continue
                    if place[x+a][y+b] == "P":
                        if place[x+c][y+d] != "X":
                            return False
                for a, b, c, d, e, f in [1,1,0,1,1,0], [1,-1,1,0,0,-1], [-1,1,0,1,-1,0], [-1,-1,-1,0,0,-1]:
                    if x+a<0 or x+a>4 or y+b<0 or y+b>4: continue
                    if place[x+a][y+b] == "P":
                        if place[x+c][y+d] != "X" or place[x+e][y+f] != "X":
                            return False
                y += 1
            else: y += 1
        x += 1
    return True