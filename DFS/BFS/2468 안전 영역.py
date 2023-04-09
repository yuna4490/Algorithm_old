import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(height, i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))

result = 0
max_value = 0
for i in range(N):
    for j in range(N):
        max_value = max(max_value, graph[i][j])

for k in range(max_value):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > k and not visited[i][j]:
                bfs(k, i, j)
                cnt += 1

    result = max(result, cnt)

print(result)