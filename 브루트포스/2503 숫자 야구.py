from itertools import permutations
n = int(input())

nums = list(permutations(range(1, 10), 3))


for _ in range(n):
    x, s, b = map(int, input().split())
    x = str(x)
    rmcnt = 0
    for i in range(len(nums)):
        strike = ball = 0
        i -= rmcnt # 매번 nums[0]부터 시작하기 위해
        for j in range(3):
            if str(nums[i][j]) == x[j]:
                strike += 1
            
            elif str(x[j]) in str(nums[i]):
                ball += 1
        
        if (strike != s) or (ball != b):
            nums.remove(nums[i])
            rmcnt += 1

print(len(nums))