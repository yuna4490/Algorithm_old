import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * n
result = []

def backtracking(k, start):
    if k == m:
        print(*result)
        return
    
    for i in range(start, len(visited)):
        if not visited[i]:
            visited[i] = True
            result.append(i+1)
            backtracking(k+1, i)
            visited[i] = False
            result.pop()
            
backtracking(0, 0)