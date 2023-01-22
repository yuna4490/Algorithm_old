import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
colors = [list(input().rstrip()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt1, cnt2 = 0, 0

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    global cnt1
    global cnt2

    queue = deque()
    queue.append((x, y))

    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if colors[x][y] == colors[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if colors[i][j] == 'G':
            colors[i][j] = 'R'

visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1


print(cnt1, cnt2)