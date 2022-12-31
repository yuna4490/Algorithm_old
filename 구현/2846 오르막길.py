n = int(input())
x = list(map(int, input().split()))
temp = 0
result = 0
for i in range(0, len(x)-1):
    if x[i] < x[i+1]:
        temp += x[i+1] - x[i]
    
    else:
        temp = 0
    
    result = max(result, temp)

print(result)

            
    
