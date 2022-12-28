from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
index = []
flag, result = 0, 0

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    queue = deque()

    for i in index:
        queue.append((i[0], i[1], i[2]))

    while queue:
        z, x, y = queue.popleft()

        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                index.append((i, j, k))


bfs()         

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                flag = 1
            result = max(result, graph[i][j][k])

if flag == 1:
    print(-1)

else:
    print(result - 1)
            