import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]

cnt = maze[0][0]

for i in range(1, m):
    maze[0][i] += maze[0][i-1]

for j in range(1, n):
    maze[j][0] += maze[j-1][0]

for i in range(1, n):
    for j in range(1, m):
        maze[i][j] += max(maze[i-1][j-1], maze[i-1][j], maze[i][j-1])

print(maze[n-1][m-1])