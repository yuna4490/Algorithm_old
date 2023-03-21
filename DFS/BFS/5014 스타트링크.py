import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

button = [U, -D]

visited = [0] * (F+1)
result = sys.maxsize

def bfs(v):
    global result
    queue = deque()
    queue.append((v, 0))
    visited[v] = 1

    while queue:
        x, cnt = queue.popleft()

        if x == G:
            result = min(result, cnt)
        
        for i in range(2):
            nx = x + button[i]

            if 0 < nx <= F and not visited[nx]:
                queue.append((nx, cnt+1))
                visited[nx] = 1

bfs(S)

if result == sys.maxsize:
    print("use the stairs")
else: 
    print(result)