import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
result = []

def dfs(v, x):
    visited[v] = 1

    for i in graph[v]:
        if not visited[i]:
            dfs(i, x)

        elif visited[i] and i == x:
            result.append(i)

for i in range(1, n+1):
    graph[int(input())].append(i)

for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i, i) 

print(len(result))
for i in result:
    print(i)