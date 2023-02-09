import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []

def backtracking(k, start):
    if k == m:
        print(*result)
        return
    
    for i in range(start, n+1):
        result.append(i)
        backtracking(k+1, i)
        result.pop()

backtracking(0, 1)