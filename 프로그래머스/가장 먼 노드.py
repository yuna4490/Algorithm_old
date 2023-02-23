from collections import deque

def solution(n, edge):
    answer = 0
    result = []
    
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)
    
    queue = deque([1])
    visited[1] = 1
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] += visited[v] + 1
                queue.append(i)
    
    max_value = max(visited)
    
    return visited.count(max_value)