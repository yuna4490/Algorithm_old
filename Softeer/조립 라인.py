import sys
input = sys.stdin.readline

n = int(input())
line = [list(map(int, input().split())) for _ in range(n-1)]
finish = list(map(int, input().split()))

time_a = 0
time_b = 0
work_a = 0
work_b = 0

for i in range(n-1):
    if n == 1:
        break

    time_a = min(line[i][0] + work_a, line[i][1] + line[i][3] + work_b)
    time_b = min(line[i][1] + work_b, line[i][0] + line[i][2] + work_a)
    work_a = time_a
    work_b = time_b

time_a += finish[0]
time_b += finish[1]

print(min(time_b, time_a))