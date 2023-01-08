import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
d = deque()

for _ in range(n):
    x = list(input().split())

    if x[0] == 'push_front':
        d.appendleft(int(x[1]))
    
    elif x[0] == 'push_back':
        d.append(int(x[1]))
    
    elif x[0] == 'pop_front':
        if d:
            print(d.popleft())
        else:
            print(-1)
    
    elif x[0] == 'pop_back':
        if d:
            print(d.pop())
        else:
            print(-1)
    
    elif x[0] == 'size':
        print(len(d))
    
    elif x[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    
    elif x[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    
    else:
        if d:
            print(d[-1])
        else:
            print(-1)
