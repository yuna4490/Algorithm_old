import sys
input = sys.stdin.readline



def sudoku(arr):
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            col[arr[i][j]] += 1
            if col[arr[i][j]] == 2:
                return 0
        
            row[arr[j][i]] += 1
            if row[arr[j][i]] == 2:
                return 0
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            sqr = [0] * 10
            for a in range(3):
                for b in range(3):
                    sqr[arr[a][b]] += 1
                    if sqr[arr[a][b]] == 2:
                        return 0
    
    return 1
     

                
T = int(input())
for i in range(1, T+1):
    sdo = [list(map(int, input().split())) for _ in range(9)]

    result = sudoku(sdo)
    print('#' + str(i), result)
    
    