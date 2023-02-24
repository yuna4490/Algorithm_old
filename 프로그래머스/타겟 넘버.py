def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for number in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + number)
            tmp.append(parent - number)
        
        leaves = tmp
    
    for leaf in leaves:
        if leaf == target:
            answer += 1
        
    return answer