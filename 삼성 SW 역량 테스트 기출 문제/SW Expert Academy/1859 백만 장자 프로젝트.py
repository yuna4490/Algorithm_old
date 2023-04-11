import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    max_price = 0
    answer = 0

    for price in prices[::-1]:
        if max_price <= price:
            max_price = price
        
        else:
            answer += max_price - price
    
    print('#' + str(i+1), answer)