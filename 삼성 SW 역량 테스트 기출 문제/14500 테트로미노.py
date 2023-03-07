import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
result = 0

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt, sum):
    global result
    if cnt == 4:
        result = max(result, sum)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:       
            if cnt == 2:
                visited[nx][ny] = 1
                dfs(x, y, cnt + 1, sum + graph[nx][ny])
                visited[nx][ny] = 0
            
            visited[nx][ny] = 1
            dfs(nx, ny, cnt + 1, sum + graph[nx][ny])
            visited[nx][ny] = 0


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j, 0, 0)
            visited[i][j] = 0

print(result)