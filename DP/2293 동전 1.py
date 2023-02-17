import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))
dp = [0] * (k+1)
dp[0] = 1 # 하나로만 만들 수 있는 경우

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])
