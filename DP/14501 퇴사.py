n = int(input())
t = []
p = []
dp = [0] * (n+1)

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1): # 뒤에서부터 검사
    if i + t[i] > n: # 검사가 마지막 날을 넘어간다면
        dp[i] = dp[i+1] # 검사 진행 x 다음 날 값 그대로 가져옴
    
    else:
        dp[i] = max(dp[t[i] + i] + p[i], dp[i+1]) # 오늘 상담을 할 경우와 안 할 경우 중 최댓값 검사

print(dp[0])