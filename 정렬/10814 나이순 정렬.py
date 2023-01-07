n = int(input())
dic = {}

for i in range(n):
    age, name = input().split()
    dic[i] = (int(age), name, i)

d = sorted(dic.values(), key = lambda x: (x[0], x[2]))

for i in d:
    print(i[0], i[1])