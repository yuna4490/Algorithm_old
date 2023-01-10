#계수정렬, Python3로 제출해야 메모리초과 안남..
import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * 10001

for _ in range(n):
    nums[int(input())] += 1

for i in range(1, 10001):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i)