from itertools import permutations

def solution(numbers):
    answer = 0
    nums = [n for n in numbers]
    per = []
    
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))
    
    per = set([int(''.join(p)) for p in per])
    
    for p in per:
        flag = 0
        if p < 2:
            continue
        
        for i in range(2, p):
            if p % i == 0:
                flag = 1
                break
        
        if flag == 0:
            answer += 1
            
    return answer