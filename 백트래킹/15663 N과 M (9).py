import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False] * n
nums.sort()
result = []

def backtracking(k):
    if k == m:
        print(*result)
        return

    remember = 0
    for i in range(n):
        if not visited[i] and remember != nums[i] :
            visited[i] = True
            result.append(nums[i])
            remember = nums[i]
            backtracking(k+1)
            visited[i] = False
            result.pop()

backtracking(0)