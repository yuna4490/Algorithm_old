import math
import sys
input = sys.stdin.readline

n, k = map(int ,input().split())

result = math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

print(result)
