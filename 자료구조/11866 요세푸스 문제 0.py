from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque(i for i in range(1, n+1))
result = []
cnt = 0
while queue:
    cnt += 1
    if cnt == k:
        result.append(queue.popleft())
        cnt = 0
    
    else:
        queue.append(queue.popleft())

print("<", end = '')
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end = '')
        print(">")
        break
    
    print(result[i], end = ", ")
