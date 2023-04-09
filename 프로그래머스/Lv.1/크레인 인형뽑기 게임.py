def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                x = board[i][move-1]
                board[i][move-1] = 0
                
                if not stack:
                    stack.append(x)
                    break
                else:
                    if stack[-1] == x:
                        stack.pop()
                        answer += 2
                        break
                        
                    else:
                        stack.append(x)
                        break
                        
    return answer