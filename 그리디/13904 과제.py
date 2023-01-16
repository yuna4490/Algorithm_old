import sys
input = sys.stdin.readline

n = int(input())
checked = [False] * 1001
hws = []
result = 0

for _ in range(n):
    d, w = map(int, input().split())
    hws.append((d, w))

hws = sorted(hws, key = lambda x : (x[1], x[0]), reverse=True)

for i in range(n):
    d = hws[i][0]
    w = hws[i][1]
    for j in range(d-1, -1, -1):
        if not checked[j]:
            checked[j] = True
            result += w
            break

print(result)