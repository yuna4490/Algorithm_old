def solution(dartResult):
    num = ''
    score = []
    
    for i in dartResult:
        if i.isdigit():
            num += i
        
        elif i == 'S':
            num = int(num) ** 1
            score.append(num)
            num = ''
        
        elif i == 'D':
            num = int(num) ** 2
            score.append(num)
            num = ''
        
        elif i == 'T':
            num = int(num) ** 3
            score.append(num)
            num = ''
        
        elif i == '*':
            if len(score) > 1:
                score[-1] *= 2
                score[-2] *= 2
            
            else:
                score[-1] *= 2
        
        else:
            score[-1] = -(score[-1])
    
    return sum(score)