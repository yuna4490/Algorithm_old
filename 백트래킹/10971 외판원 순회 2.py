import sys
input = sys.stdin.readline

n = int(input())
W = [list(map(int, input().split())) for _ in range(n)]
result = sys.maxsize
visited = [0] * n

def backtracking(start, now, cnt, sum):
    global result
    if cnt == n:
        if W[now][start]:
            result = min(result, sum + W[now][start])
        return
    
    for i in range(n):
        if not visited[i] and W[now][i]:
            visited[i] = 1
            backtracking(start, i, cnt + 1, sum + W[now][i])
            visited[i] = 0

# start 설정
for i in range(n):
    visited[i] = 1
    backtracking(i, i, 1, 0)
    visited[i] = 0

print(result)