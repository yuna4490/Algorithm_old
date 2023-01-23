import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rank = [input().split() for _ in range(n)]

def bs(x):
    low, high = 0, len(rank)-1
    result = 0

    while low <= high:
        mid = (low + high) // 2

        if int(rank[mid][1]) >= x:
            high = mid - 1
            result = mid
        
        else:
            low = mid + 1
    
    return result

for _ in range(m):
    power = int(input())
    print(rank[bs(power)][0])