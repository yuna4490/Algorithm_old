import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []
visited = []
result = sys.maxsize

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append((i, j))
        
        elif graph[i][j] == 1:
            houses.append((i, j))

def backtracking(cnt, start):
    if cnt == m:
        global result
        sum = 0
        for i, j in houses:
            min_distance = sys.maxsize
            for a, b in visited:
                distance = abs(i - a) + abs(j - b)
                min_distance = min(min_distance, distance)
        
            sum += min_distance
        result = min(result, sum)
        return
    
    for i in range(start, len(chickens)):
        if chickens[i] not in visited:
            visited.append(chickens[i])
            backtracking(cnt + 1, i + 1)
            visited.pop()

backtracking(0, 0)
print(result)