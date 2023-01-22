import sys
input = sys.stdin.readline

n = int(input()) # 지방의 수
money = list(map(int, input().split()))
m = int(input()) # 총 예산

m_m = max(money)
low, high = 1, m_m

while low <= high:
    mid = (low + high) // 2
    sum = 0

    for i in money:
        if i > mid:
            sum += mid
        
        else:
            sum += i
    
    if sum == m:
        high = mid
        break

    elif sum > m:
        high = mid - 1

    else:
        low = mid + 1

if m_m > high:
    print(high)

else:
    print(m_m)
