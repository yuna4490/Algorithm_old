import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]

low, high = 1, max(lines)
while low <= high:
    mid = (low + high) // 2

    cnt = 0
    for line in lines:
        cnt += (line // mid)
    
    if cnt >= n:
        low = mid + 1

    else:
        high = mid - 1
    
print(high)