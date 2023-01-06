import sys
input = sys.stdin.readline

result = 0
for i in range(5):
    first, last = input().split()
    xh = int(first[0:2])
    yh = int(last[0:2])
    xm = int(first[3:5])
    ym = int(last[3:5])
    result += (yh*60 + ym) - (xh*60 + xm)

print(result)