import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, idx = map(int, input().split())
    queue = list(map(int, input().split()))
    index = [0 for i in range(n)]
    index[idx] = 1

    cnt = 0
    while queue:
        if queue[0] == max(queue):
            cnt += 1
            if index[0] == 1:
                print(cnt)
                break

            else:
                queue.pop(0)
                index.pop(0)
        
        else:
            queue.append(queue.pop(0))
            index.append(index.pop(0))