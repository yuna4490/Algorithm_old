from collections import deque
n = int(input())
queue = deque([i for i in range(1, n+1)])

while queue:
    if len(queue) == 1:
        break

    queue.popleft()
    queue.append(queue.popleft())

print(*queue)