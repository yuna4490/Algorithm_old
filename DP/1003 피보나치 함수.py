import sys
input = sys.stdin.readline

dp_0 = [1, 0]
dp_1 = [0, 1]

def fibonacci(n):
    length = len(dp_0)
    if n >= length:
        for i in range(length, n+1):
            dp_0.append(dp_0[i-1] + dp_0[i-2])
            dp_1.append(dp_1[i-1] + dp_1[i-2])
    
    print(dp_0[n], dp_1[n])

t = int(input())
for _ in range(t):
    fibonacci(int(input()))
    
    