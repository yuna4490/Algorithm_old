import sys
import math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0

for i in a:
    if i > b:
        i -= b
        cnt += 1
        cnt += math.ceil(i/c)
    
    else:
        cnt += 1

print(cnt)