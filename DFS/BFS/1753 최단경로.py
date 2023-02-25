import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int ,input().split())
k = int(input()) # 시작 정점

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijstra(start):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
            
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

dijstra(k)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")

    else: 
        print(distance[i])
