import sys
input = sys.stdin.readline

n = int(input())

cnt, num = 1, 1
result = 1
while n > num:
    num += cnt * 6
    result += 1
    cnt += 1

print(result)