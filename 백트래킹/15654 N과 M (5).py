import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []

def backtracking(k):
    if k == m:
        print(*result)
        return
    
    for num in nums:
        if num not in result:
            result.append(num)
            backtracking(k+1)
            result.pop()

backtracking(0)