from collections import defaultdict
import math

def solution(fees, records):
    d = defaultdict(list)
    check = defaultdict(int)
    result = []
    
    for record in records:
        time = record[0:5]
        if time[0] == '0':
            h = time[1]
        else:    
            h = time[0:2]
            
        m = time[3:]
        t = int(h) * 60 + int(m)

        if record[11:] == 'IN':
            d[int(record[6:10])].append(t)
            check[int(record[6:10])] = 0
        
        else:
            t -= d[int(record[6:10])][-1]
            d[int(record[6:10])][-1] = t
            check[int(record[6:10])] = 1

    dic = sorted(d.items())
    c = sorted(check.items())

    for i in dic:
        idx = dic.index(i)
        if c[idx][1] == 0:
            i[1][-1] = 1439 - i[1][-1]
    
        time = sum(i[1])
        fee = 0
        
        if time > fees[0]:
            fee = fees[1]
            time -= fees[0]
            fee += (math.ceil(time/fees[2])) * fees[3]
        
        else:
            fee = fees[1]
        
        result.append(fee)
        
    return result