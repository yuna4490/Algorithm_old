import sys
import time
input = sys.stdin.readline

m, n = map(int, input().split())
t = int(n**0.5)

# 1은 소수가 아니므로 2부터 시작
# m == 3이면 2를 건너뛰어 2의 배수도 출력되므로 2부터 시작
if m == 1 or m == 3:
    m = 2
arr = [True] * (n+1)
for i in range(m, t+1):
    if arr[i] == True:
        for j in range(i+i, n+1, i):
            arr[j] = False

for i in range(m, n+1):
    if arr[i] == True:
        print(i)

