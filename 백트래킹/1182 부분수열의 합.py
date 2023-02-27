import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
def backtracking(sum, num):
    global cnt

    if num >= n:
        return

    sum += nums[num]
    
    if sum == s:
        cnt += 1
    
    backtracking(sum, num + 1) # 현재 값 집어넣고 다음 값으로 넘어감
    backtracking(sum - nums[num], num + 1) # 현재 값 안 집어넣고 다음 값으로 넘어감
    
backtracking(0, 0)
print(cnt)
