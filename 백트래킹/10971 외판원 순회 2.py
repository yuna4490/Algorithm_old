import sys
input = sys.stdin.readline

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]

visited = [0] * n
result = sys.maxsize

def dfs(start, now, cnt, sum):
    global result
    if cnt == n:
        if W[now][start]:
            sum += W[now][start]
        
            result = min(result, sum)
        return
    
    for i in range(n):
        if not visited[i] and W[now][i]:
            visited[i] = 1
            dfs(start, i, cnt+1, sum + W[now][i])
            visited[i] = 0

# start 설정
for i in range(n):
    visited[i] = 1
    dfs(i, i, 1, 0)
    visited[i] = 0

print(result)