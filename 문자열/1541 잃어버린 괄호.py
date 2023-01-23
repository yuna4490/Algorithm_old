import sys
input = sys.stdin.readline

arr = input().rstrip().split('-')
nums = []

for i in arr:
    tmp = i.split('+')
    sum = 0
    for j in tmp:
        sum += int(j)  
    nums.append(sum)

result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]

print(result)
    