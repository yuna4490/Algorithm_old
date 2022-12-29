n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)


def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)