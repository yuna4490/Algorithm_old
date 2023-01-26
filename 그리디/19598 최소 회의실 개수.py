import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort()

heapq.heappush(heap, meetings[0][1])

for i in range(1, n):
    if meetings[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, meetings[i][1])
        
    else:
        heapq.heappush(heap, meetings[i][1])
        
print(len(heap))
