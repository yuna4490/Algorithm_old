import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt1, cnt2, cnt3 = 0, 0, 0

def cut(x, y, n):
    global cnt1, cnt2, cnt3
    num = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                cut(x, y, n//3)
                cut(x, y + n//3, n//3)
                cut(x, y + 2*n//3, n//3) 
                cut(x + n//3, y, n//3)
                cut(x + 2*n//3, y, n//3)
                cut(x + n//3, y + n//3, n//3)
                cut(x + n//3, y + 2*n//3, n//3)
                cut(x + 2*n//3, y + n//3, n//3)
                cut(x + 2*n//3, y + 2*n//3, n//3)
                return
    
    if num == -1:
        cnt1 += 1
    
    elif num == 0:
        cnt2 += 1
    
    else:
        cnt3 += 1

cut(0, 0, n)
print(cnt1)
print(cnt2)
print(cnt3)
