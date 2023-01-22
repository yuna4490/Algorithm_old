import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    dic = dict()
    n = int(input())
    
    for _ in range(n):
        a, b = input().split()
        
        if dic.get(b) == None:
            dic[b] = set()
        
        dic[b].add(a)
    
    result = 1
    for key in dic.keys():
        result *= (len(dic[key]) + 1)
    
    print(result - 1)