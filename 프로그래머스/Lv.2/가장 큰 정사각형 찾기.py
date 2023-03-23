def solution(board):
    max_length = board[0][0] # 중요!
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                max_length = max(max_length, board[i][j])

    return max_length**2