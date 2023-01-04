import sys
input = sys.stdin.readline

n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))
result = []

for i in range(k):
    sum = 0
    a, b = map(int, input().split())
    x = s[a:b+1]

    for j in x:
        sum += j
    result.append(round(sum/len(x), 2))

for i in result:
    print(format(i, ".2f"))