def dfs(x, visited, computers, n):

    for i in range(n):
        if not visited[i] and computers[x][i] == 1:
            visited[i] = 1
            dfs(i, visited, computers, n)     
    
def solution(n, computers):
    answer = 0
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(i, visited, computers, n)
            answer += 1
        
    return answer