import sys
from itertools import permutations
n = int(input())
A = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = ['+', '-', '*', '/']
op = []

for i in range(len(arr1)):
    for j in range(arr1[i]):
        op.append(arr2[i])

per = list(permutations(op, n-1))

maximum = -1e9
minimum = 1e9

for p in per:
    result = A[0]
    for i in range(1, n):
        if p[i-1] == '+':
            result += A[i]
        
        elif p[i-1] == '-':
            result -= A[i]
        
        elif p[i-1] == '*':
            result *= A[i]
        
        elif p[i-1] == '/':
            result = int(result / A[i])

    if result > maximum:
        maximum = result
    
    if result < minimum:
        minimum = result

print(maximum)
print(minimum)