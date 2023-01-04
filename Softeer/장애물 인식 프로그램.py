# bfs
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    graph[i][j] = 0
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
