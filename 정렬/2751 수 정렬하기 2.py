n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()
for i in nums:
    print(i)