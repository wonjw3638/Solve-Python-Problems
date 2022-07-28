def cal_fee(i,j):
    time = (int(j.split(':')[0])*60+int(j.split(':')[1]))-(int(i.split(':')[0])*60+int(i.split(':')[1]))
    return time

def solution(fees, records):
    id_list = []
    for i in records:
        id_list.append(i.split()[1])
    id_list.sort(key=int)
    car = []
    for i in id_list:
        if i not in car:
            car.append(i)
            
    id = { x:0 for x in car }

    for i in records:
        if i.split()[2] == "IN":
            num = i.split()[1]
            check = 0
            for j in range(records.index(i)+1, len(records)+1):
                if records[j-1].split()[2] ==  "OUT" and records[j-1].split()[1]==i.split()[1]:
                    time = cal_fee(i.split()[0],records[j-1].split()[0])
                    check += 1
                    id[i.split()[1]] += time
                    break
            if check == 0:
                time = cal_fee(i.split()[0],"23:59")
                id[i.split()[1]] += time
                
    answer = []
    for i in car:
        time = int(id["{}".format(i)])
        if int(time) <= fees[0]:
            answer.append(fees[1])
        else:
            if (int(time)-fees[0])%fees[2] == 0:
                a = 0
            else:
                a = 1
            total = fees[1] + ((int(time)-fees[0])//fees[2]+a)*fees[3]
            answer.append(total)
    return answer