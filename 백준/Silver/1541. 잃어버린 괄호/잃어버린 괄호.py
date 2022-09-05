string = input()
numbers = [ str(i) for i in range(10)]

answer = sum_num = sub_num = 0
sub = False
tmp = ''

for s in string:
    if s in numbers:
        tmp += s
    else:
        if sub == True:
            sub_num += int(tmp)
            tmp = ''
        else:
            sum_num += int(tmp)
            tmp = ''

        if s == '-':
            sub = True
            
if sub == True:
    sub_num += int(tmp)
    tmp = ''
else:
    sum_num += int(tmp)
    tmp = ''

answer = sum_num - sub_num

print(answer)