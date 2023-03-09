x = input().lower()

dic = dict()

for i in x:
    if dic.get(i) == None:
        dic[i] = 0
    
    else:
        dic[i] += 1

max_use = max(dic.values())

cnt = 0
result = ''
for d in dic.keys():
    if dic[d] == max_use:
        cnt += 1
        result = d

if cnt > 1:
    print('?')

else:
    print(result.upper())
