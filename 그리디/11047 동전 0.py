import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = [int(input()) for _ in range(n)]
cnt = 0

for i in reversed(range(n)):
    cnt += k//values[i] #카운트 값에 k를 동전으로 나눈 몫 더해줌
    k %= values[i] #k는 동전으로 나눈 나머지로 계속 반복

print(cnt)