# dp
import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * n
rocks = list(map(int, input().split()))
dp[0] = 0

for i in range(0, n):
    for j in range(0, i):
        if rocks[j] < rocks[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    
    dp[i] += 1

print(max(dp))