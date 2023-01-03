from collections import deque

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] += 1
    

while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    
    print(cnt)
    
