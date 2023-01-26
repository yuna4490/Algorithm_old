import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rank = [input().split() for _ in range(n)]

for _ in range(m):
    power = int(input())
    low, high = 0, n-1
    result = 0

    while low <= high:
        mid = (low + high) // 2
        if int(rank[mid][1]) >= power:
            high = mid - 1
            result = mid
        
        else:
            low = mid + 1
    
    print(rank[result][0])