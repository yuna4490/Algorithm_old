import sys
import copy
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

def bfs():
    tmp_graph = copy.deepcopy(graph)
    queue = deque()
    global result

    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0:
                queue.append((nx, ny))
                tmp_graph[nx][ny] = 2

    sum = 0
    for i in range(n):
        sum += tmp_graph[i].count(0)
    
    result = max(result, sum)


def backtracking(cnt):
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                backtracking(cnt+1)
                graph[i][j] = 0

backtracking(0)
print(result)