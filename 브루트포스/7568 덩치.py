import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
rank = [1] * n
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            rank[i] += 1


print(*rank)