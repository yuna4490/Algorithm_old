import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

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

dijstra(c)

time = 0
cnt = 0
for d in distance:
    if d != INF:
       cnt += 1
       time = max(time, d)

print(cnt - 1, time) # 시작 노드는 제외해야 하므로 -1 
