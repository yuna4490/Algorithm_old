import sys
input = sys.stdin.readline

c = int(input())
result = 0

def backtracking(cnt, sum):
    global result
    if cnt == 11:
        result = max(result, sum)
        return
    
    for i in range(11):
        if positions[i] or not s[cnt][i]:
            continue
        
        positions[i] = 1
        backtracking(cnt+1, sum + s[cnt][i])
        positions[i] = 0


for _ in range(c):
    s = [list(map(int, input().split())) for _ in range(11)]
    positions = [0] * 11

    backtracking(0, 0)
    print(result)