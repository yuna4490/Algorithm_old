from collections import deque
import sys

input = sys.stdin.readline

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while queue:
        z, x, y = queue.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and graph[nz][nx][ny] == 0:
                queue.append((nz, nx, ny))
                graph[nz][nx][ny] = graph[z][x][y] + 1

queue = deque()              
for i in range(h):
    for j in range(n):
        for k in range(m):
            # 높이, x,y 순서
            if graph[i][j][k] == 1:
                # 높이, x,y 순서
                queue.append((i,j,k))

bfs()

flag = 0
result = -2


for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 0:
                flag = 1
            result = max(result, graph[i][j][k])

if flag == 1: # 모두 익지 못한 상태 
    print(-1)

elif result == 1: # 모두 익어있던 상태
    print(0)

else:
    print(result - 1) # 처음 시작이 1이어서 하루 지났을 때 2가 저장되기 때문에.. -1 해줘야 함