def dfs(v, visited, computers):
    visited[v] = 1
    for i in range(len(computers)):
        if computers[v][i] == 1 and not visited[i]:
            visited[i] = 1
            dfs(i, visited, computers)
            

def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, computers)
            answer += 1
        
    return answer