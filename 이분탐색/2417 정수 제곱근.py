import sys
input = sys.stdin.readline

n = int(input())

low, high = 0, n
result = 0
checked = False

while low <= high:
    mid = (low + high) // 2

    if mid**2 > n:
        high = mid - 1
    
    elif mid**2 < n:
        low = mid + 1

    else:
        result = mid
        checked = True
        break

if not checked:
    if high*high < n:
        result = high + 1
    else:
        result = high
        
print(result)
