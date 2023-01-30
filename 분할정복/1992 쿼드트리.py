import sys
input = sys.stdin.readline

n = int(input())
video = [list(input().rstrip()) for _ in range(n)]
result = []

def qt(x, y, n):
    data = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if data != video[i][j]:
                result.append('(')
                qt(x, y, n//2)
                qt(x, y + n//2, n//2)
                qt(x + n//2, y, n//2)
                qt(x + n//2, y + n//2, n//2)
                result.append(')')
                return
    
    if data == '0':
        result.append(0)
    
    else:
        result.append(1)

qt(0, 0, n)
print(*result, sep = '')