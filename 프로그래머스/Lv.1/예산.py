def solution(d, budget):
    answer = 0
    sum = 0
    d.sort()
    
    for i in d:
        if sum + i <= budget:
            sum += i
            answer += 1
        
        else:
            break
            
    return answer