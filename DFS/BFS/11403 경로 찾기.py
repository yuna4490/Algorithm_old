import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n): # 거쳐가는 노드
    for i in range(n): # 출발하는 노드
        for j in range(n): # 도착하는 노드
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for i in graph:
    print(*i)

