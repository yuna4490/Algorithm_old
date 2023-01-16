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
    if s >= tmp:
        tmp = f
        cnt += 1

print(cnt)