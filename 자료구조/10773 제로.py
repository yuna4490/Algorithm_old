k = int(input())
stack = []

for _ in range(k):
    num = int(input())

    if num == 0:
        stack.pop()
    
    else:
        stack.append(num)

if not stack:
    print(0)

else:
    print(sum(stack))