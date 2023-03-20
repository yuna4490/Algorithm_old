import sys
input = sys.stdin.readline

INF = int(1e9)
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a-1][b-1] = l
    graph[b-1][a-1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0

            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0

for i in range(n):
    sum = 0
    for j in range(n):
        if graph[i][j] <= m:
            sum += items[j]
    
    result = max(result, sum)

print(result)