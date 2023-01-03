import sys
input = sys.stdin.readline

w, n = map(int, input().split())
arr = []
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))

arr = sorted(arr, key = lambda x : x[1], reverse = True)
result = 0

for m, p in arr:
    if m <= w:
        w -= m
        result += m * p
    
    else:
        result += w * p
        break

print(result)