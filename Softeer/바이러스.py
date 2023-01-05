import sys
input = sys.stdin.readline

k, p, n = map(int, input().split())

# 1초당 p배씩 불어남

for _ in range(n):
    k *= p
    k %= 1000000007

print(k)