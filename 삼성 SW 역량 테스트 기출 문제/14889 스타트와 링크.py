import sys
input = sys.stdin.readline

n = int(input())
powers = [list(map(int, input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
min_diff = 0

def backtracking(cnt, idx):
    global min_diff
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += powers[i][j] + powers[j][i]
                
                elif not visited[i] and not visited[j]:
                    link += powers[i][j] + powers[j][i]

        min_diff = min(min_diff, abs(start - link))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            backtracking(cnt+1, i+1)

backtracking(0, 0)
print(min_diff)