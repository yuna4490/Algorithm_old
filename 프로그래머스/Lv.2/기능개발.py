import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()
    
    for p, s in zip(progresses, speeds):
        days.append(math.ceil((100 - p) / s))
    
    while days:
        v = days.popleft()
        cnt = 1
        
        while days and v >= days[0]:
            days.popleft()
            cnt += 1
        
        answer.append(cnt)
        
    return answer