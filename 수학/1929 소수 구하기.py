import sys
import time
input = sys.stdin.readline

m, n = map(int, input().split())
t = int(n**0.5)

arr = [True] * (n+1)
for i in range(2, t+1):
    if arr[i] == True:
        for j in range(i+i, n+1, i):
            arr[j] = False

for i in range(m, n+1):
    if i != 1 and arr[i] == True:
        print(i)

