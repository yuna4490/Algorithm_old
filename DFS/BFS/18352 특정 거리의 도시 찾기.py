import heapq
import sys
input = sys.stdin.readline
INF = 1e9

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1)) # 거리는 1이라고 생각

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


dijstra(x)

result = []
for i in range(len(distance)):
    if distance[i] == k:
        result.append(i)

if not result:
    print(-1)

else:
    result.sort()
    for i in result:
        print(i)
