import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[n for _ in range(n)] for _ in range(n)]
result = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0

            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    result.append(sum(graph[i]))

print(result.index(min(result)) + 1)