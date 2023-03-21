import heapq

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
        

def solution(N, road, K):
    answer = 0

    INF = int(1e9)
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    dijstra(1, distance, graph)
    
    for i in distance[1:]:
        if i <= K:
            answer += 1

    return answer