def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i
        
            if yellow_x >= yellow_y and yellow_x * 2 + yellow_y * 2 + 4 == brown:
                return [yellow_x + 2, yellow_y + 2]
            