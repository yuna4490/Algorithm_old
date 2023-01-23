import sys
import heapq
input = sys.stdin.readline

classes = []
n = int(input())
for _ in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))

classes.sort() # 수업 시작 시간 순으로 오름차순 정렬

heap = []
heapq.heappush(heap, classes[0][1]) # 첫 수업의 끝나는 시간 heap에 저장

for i in range(1, n):
    if classes[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, classes[i][1])
    
    else:
        heapq.heappush(heap, classes[i][1])

print(len(heap))