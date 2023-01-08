import sys
input = sys.stdin.readline

while True:
    string = input().rstrip()
    
    if string == ".":
        break

    stack = []
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            
            else:
                stack.append(i)
                break
        
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print("yes")

    else:
        print("no")