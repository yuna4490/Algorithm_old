# 1
def solution(numbers, target):
    answer = 0
    leaves = [0]
    
    for number in numbers:
        tmp = []
        
        for leaf in leaves:
            tmp.append(leaf + number)
            tmp.append(leaf - number)
        
        leaves = tmp
    
    answer = leaves.count(target)
    
    return answer

# 2
from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque()
    queue.append((numbers[0], 0)) # 합, index
    queue.append((-numbers[0],0))
    
    while queue:
        xsum, idx = queue.popleft()
        idx += 1
        
        if idx < len(numbers):
            queue.append((xsum + numbers[idx], idx))
            queue.append((xsum - numbers[idx], idx))  
        
        else:
            if xsum == target:
                answer += 1
        
    return answer