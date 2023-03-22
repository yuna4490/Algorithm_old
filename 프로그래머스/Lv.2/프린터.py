#1 
from collections import deque
def solution(priorities, location):
    answer = 0
    
    queue = deque()
    
    for p in priorities:
        queue.append(p)
    
    while queue:
        if location == 0:
            if queue[location] == max(queue):
                answer += 1
                return answer
            
            else:
                queue.append(queue.popleft())
                location = len(queue) - 1
        
        else:
            p = queue.popleft()
            if p < max(queue):
                queue.append(p)
            
            else:
                answer += 1
            
            location -= 1

#2 enumerate 활용
from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    # (idx, p) 튜플로 이루어진 deque 생성
    
    while queue:
        x = queue.popleft()
        if queue and x[0] < max(queue)[0]:
            queue.append(x)
        
        else:
            answer += 1 
            if x[1] == location:
                break
    
    return answer