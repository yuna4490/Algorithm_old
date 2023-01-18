import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

low, high = 1, max(trees)

while low <= high:
    sum = 0
    mid = (low + high) // 2
    
    for tree in trees:
        if tree > mid:
            sum += (tree - mid)

    if sum >= m:
        low = mid + 1
    
    else:
        high = mid - 1

print(high)