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

    visited = [False] * n
    remember = 0
    for i in range(start, n):
        if not visited[i] and remember != nums[i]:
            visited[i] = True
            result.append(nums[i])
            remember = nums[i]
            backtracking(k+1, i)
            visited[i] = False
            result.pop()

backtracking(0, 0)