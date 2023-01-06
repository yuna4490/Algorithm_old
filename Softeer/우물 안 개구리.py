import sys
input = sys.stdin.readline

n, m = map(int, input().split())
w = [0] + list(map(int, input().split()))
best = [1] * (n+1)
result = 0

for _ in range(m):
    a, b = map(int, input().split())

    if w[a] > w[b]:
        best[b] = 0
    
    elif w[b] > w[a]:
        best[a] = 0

    else:
        best[a] = 0
        best[b] = 0

for i in range(best):
    if i == 1:
        result += 1

print(result)