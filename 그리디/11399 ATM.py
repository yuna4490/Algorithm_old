import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()
result = 0
for i in range(n):
    sum = 0
    for j in range(0, i+1):
        sum += p[j]
    result += sum

print(result)
