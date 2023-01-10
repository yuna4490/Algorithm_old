# 딕셔너리 방법 / Counter 라이브러리
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

c = Counter(nlist)
# print(' '.join(f'{c[m]}' if m in c else '0' for m in mlist))

for m in mlist:
    if m in c:
        print(c[m], end = ' ')

    else:
        print(0, end = ' ')