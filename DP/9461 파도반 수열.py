import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0] * n
    
    if n <= 2:
        print(1)
        continue

    else:
        dp[0], dp[1], dp[2] = 1, 1, 1
    
    for i in range(3, n):
        dp[i] = dp[i-3] + dp[i-2]
    
    print(dp[n-1])
