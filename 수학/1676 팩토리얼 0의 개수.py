import sys
import math
input = sys.stdin.readline

n = int(input())
num = math.factorial(n)
cnt = 0

num = str(num)
for i in range(len(num)-1, -1, -1):
    if num[i] == '0':
        cnt += 1
    
    else:
        print(cnt)
        break