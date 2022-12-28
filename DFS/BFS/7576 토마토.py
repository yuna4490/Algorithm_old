from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))
bfs()

flag = 0
result = -2

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = 1
        result = max(result, graph[i][j])

if flag == 1:
    print(-1)

elif result == 1:
    print(0)

else:
    print(result - 1)
    


    