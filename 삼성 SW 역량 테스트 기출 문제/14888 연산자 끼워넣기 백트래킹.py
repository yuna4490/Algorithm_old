import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
cnt = list(map(int, input().split()))
# +, -, x, /
visited = [0] * (n-1)
op = ['+', '-', '*', '/']
x = []

for i in range(4):
    for _ in range(cnt[i]):
        x.append(op[i])

max_result = -1e9
min_result = 1e9

def backtracking(cnt, value):
    global max_result
    global min_result
    if cnt == n-1:
        max_result = max(max_result, value)
        min_result = min(min_result, value)
        return
    
    for i in range(n-1):
        if not visited[i]:
            visited[i] = 1
            if x[i] == '+':
                backtracking(cnt + 1, value + A[cnt+1])
            elif x[i] == '-':
                backtracking(cnt + 1, value - A[cnt+1])
            elif x[i] == '*':
                backtracking(cnt + 1, value * A[cnt+1])
            else:
                backtracking(cnt + 1, int(value / A[cnt+1]))
            visited[i] = 0

backtracking(0, A[0])
print(max_result)
print(min_result)