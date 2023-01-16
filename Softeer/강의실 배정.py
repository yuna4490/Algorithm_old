import sys
import heapq
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    s, f = map(int, input().split())
    heapq.heappush(heap, (f, s))

tmp = 0
cnt = 0
while heap:
    f, s = heapq.heappop(heap)
    if s >= tmp: #시작시간이 이전의 끝나는 시간보다 크거나 같다면
        tmp = f
        cnt += 1

print(cnt)