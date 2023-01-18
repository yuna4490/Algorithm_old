import sys
# from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
dic1 = dict()
dic2 = dict()

for i in range(n):
    name = input().rstrip()
    dic1[i+1] = name
    dic2[name] = i+1

for i in range(m):
    x = input().rstrip()
    if x.isalpha():
        print(dic2[x])
    
    else:
        print(dic1[int(x)])
