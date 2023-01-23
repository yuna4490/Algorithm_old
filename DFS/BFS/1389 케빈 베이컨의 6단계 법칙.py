import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # 유저 수, 관계 수
graph = [[] for _ in range(n+1)] # 관계 리스트
# kb = [0 for _ in range(n+1)] # 케빈 베이컨 수 리스트

def bfs(x):
    nums = [0] * (n+1)
    visited = [0] * (n+1)
    visited[x] = 1
    
    queue = deque()
    queue.append(x)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                nums[i] = nums[v] + 1
                visited[i] = 1
                queue.append(i)

    return sum(nums)


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, n+1):
    result.append(bfs(i))

print(result.index(min(result))+ 1)