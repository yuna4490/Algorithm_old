import sys
t = int(input())

arr = [list(i for i in range(15)) for _ in range(15)]

for i in range(1, 15):
    for j in range(1, 15):
        arr[i][j] = 0
        for k in range(1, j+1):
            arr[i][j] += arr[i-1][k]

for _ in range(t):
    k = int(input())
    n = int(input())
            
    print(arr[k][n])