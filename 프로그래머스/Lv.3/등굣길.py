def solution(m, n, puddles):
    
    matrix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    matrix[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles:
                continue
            
            if matrix[i-1][j] != -1:
                matrix[i][j] += matrix[i-1][j]
            
            if matrix[i][j-1] != -1:
                matrix[i][j] += matrix[i][j-1]
    
    return matrix[n][m] % 1000000007