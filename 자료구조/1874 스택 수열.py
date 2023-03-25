import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
result = []
stack = []
visited = [0] * (n+1)

last = 1
flag = 0
for num in nums:
    if num not in stack:
        for i in range(last, num + 1):
            if not visited[i]:
                stack.append(i)
                result.append('+')
        
        last = stack.pop()
        visited[last] = 1
        result.append('-')

    else:
        if stack[-1] == num:
            last = stack.pop()
            visited[last] = 1
            result.append('-')
        
        else:
            print("NO")
            flag = 1
            sys.exit()
    
if flag == 0:
    for i in result:
        print(i)