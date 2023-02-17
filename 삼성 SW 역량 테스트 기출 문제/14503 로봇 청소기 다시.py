import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)] 

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque()
queue.append((r, c))
visited[r][c] = 1
cnt = 1

while queue:
    x, y = queue.popleft()
    flag = 0
    for _ in range(4):
        d = (d+3) % 4 # 반시계 방향
        # 해당 방향으로 전진
        nx = x + dx[d] 
        ny = y + dy[d] 

        if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]: # 청소되지 않은 칸이 있다면
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                flag = 1
                cnt += 1
                break
    
    if flag == 0: # 청소되지 않은 빈 칸이 없는 경우
        if graph[x - dx[d]][y - dy[d]] == 1:
            print(cnt)
            break
    
        else:
            queue.append((x - dx[d], y - dy[d]))
    
