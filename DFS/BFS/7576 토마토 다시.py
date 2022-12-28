from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
index = []
flag, result = 0, 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()

    for i in index:
        queue.append((i[0], i[1]))

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            index.append((i, j))


bfs()         

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            flag = 1
        result = max(result, graph[i][j])

if flag == 1:
    print(-1)

else:
    print(result - 1)
            