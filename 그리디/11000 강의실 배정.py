import sys
import heapq
input = sys.stdin.readline

heap = []
classes = []
n = int(input())
for _ in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))

classes.sort() # 시작 시간 순으로 오름차순 정렬

heapq.heappush(heap, classes[0][1]) # 첫 수업의 끝나는 시간 저장

for i in range(1, n):
    if classes[i][0] < heap[0]: # 다음 수업의 시작 시간이 이전 수업의 끝나는 시간보다 이를 경우
        heapq.heappush(heap, classes[i][1]) # 새로운 수업의 끝나는 시간 추가 (회의실 추가 배정)
    
    else:
        heapq.heappop(heap) # 같은 회의실 배정이 가능할 경우 다음 수업의 끝나는 시간으로 바꿔줌
        heapq.heappush(heap, classes[i][1])

print(len(heap))

