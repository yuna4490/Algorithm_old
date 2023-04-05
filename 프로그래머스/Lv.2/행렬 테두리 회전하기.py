def solution(rows, columns, queries):
    answer = []
    matrix = [[0 for _ in range(columns+1)] for _ in range(rows+1)]
    
    num = 1
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            matrix[row][column] = num
            num += 1
    
    
    for x1, y1, x2, y2 in queries:
        tmp = matrix[x1][y1]
        min_value = tmp
        
        for i in range(x1, x2):
            t = matrix[i+1][y1]
            matrix[i][y1] = t
            min_value = min(min_value, t)
        
        for i in range(y1, y2):
            t = matrix[x2][i+1]
            matrix[x2][i] = t
            min_value = min(min_value, t)
        
        for i in range(x2, x1, -1):
            t = matrix[i-1][y2]
            matrix[i][y2] = t
            min_value = min(min_value, t)
        
        for i in range(y2, y1, -1):
            t = matrix[x1][i-1]
            matrix[x1][i] = t
            min_value = min(min_value, t)
        
        matrix[x1][y1+1] = tmp
        answer.append(min_value)
        
    return answer