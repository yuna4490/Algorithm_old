# 다익스트라
import heapq

INF = 1e9
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

def dijstra(start, distance, graph):
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

for x, y in edge:
    graph[x].append((y, 1))
    graph[y].append((x, 1))

dijstra(1, distance, graph)

return distance.count(max(distance[1:]))


