n = int(input())
files = {} # 또는 dict()

for i in range(n):
    name, ex = input().split('.')
    
    if ex in files:
        files[ex] += 1
    
    else: files[ex] = 1

result = sorted(files.items())
for i in result:
    print(*i)