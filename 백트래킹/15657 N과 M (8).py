import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

def backtracking(k, start):
    if k == m:
        print(*result)
        return
    
    for i in range(start, len(nums)):
        result.append(nums[i])
        backtracking(k+1, i)
        result.pop()

backtracking(0, 0)