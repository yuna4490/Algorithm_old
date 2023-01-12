import sys
import math
from collections import Counter
input = sys.stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))
nums.sort()

r1 = r2 = r3 = r4 = 0

for num in nums:
    r1 += num
r1 /= n
print(int(round(r1,0)))

mid = n // 2
r2 = nums[mid]
print(r2)

c = Counter(nums)
c = sorted(c.items(), key = lambda x: x[1], reverse=True)

if n > 1:
    if c[0][1] == c[1][1]:
        r3 = c[1][0]
    else:
        r3 = c[0][0]
else:
    r3 = c[0][0]
print(r3)

if n > 1:
    r4 = max(nums) - min(nums)
else: 
    r4 = 0

print(r4)

#1. 산술평균
#2. 중앙값
#3. 최빈값
#4. 범위
