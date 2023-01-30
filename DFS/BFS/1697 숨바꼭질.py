import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
result = 100000
# 1초 후에 x-1 or x+1
# 순간이동은 1초 후에 2*x

def bfs(n, time):
    global result
    queue = deque()
    queue.append((n, time))
    visited[n] = True

    while queue:
        v, time = queue.popleft()

        if v == k:
            result = min(result, time)

        if 0 <= v-1 <= 100000 and not visited[v-1]:
            queue.append((v-1, time+1))
            visited[v-1] = True
        
        if 0 <= v+1 <= 100000 and not visited[v+1]:
            queue.append((v+1, time+1))
            visited[v+1] = True
        
        if 0 <= v*2 <= 100000 and not visited[v*2]:
            queue.append((v*2, time+1))
            visited[v*2] = True

bfs(n, 0)
print(result)