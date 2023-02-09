import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

per = list(permutations(nums, m))
for p in per:
    print(*p)