from itertools import product

n, k = map(int, input().split())
nums = list(input().split())
len_max = len(str(n))
result = []

while True:
    temp = list(product(nums, repeat = len_max))
    
    for i in temp:
        if int(''.join(i)) <= n:
            result.append(''.join(i))
    
    if len(result) >= 1:
        print(max(result))
        break

    else:
        len_max -= 1