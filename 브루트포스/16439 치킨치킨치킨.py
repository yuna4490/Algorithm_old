from itertools import combinations

n, m = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
result = 0

for a,b,c in combinations(range(m), 3):
    sum = 0
    for i in range(n):
        sum += max(p[i][a], p[i][b], p[i][c])
    
    result = max(result, sum)

print(result)
