# 실패한 코드 (효율성 테스트 실패)
def solution(people, limit):
    answer = 0
    
    while people:
        if len(people) == 1:
            answer += 1
            break
            
        x = min(people)
        y = max(people)
        
        if x + y <= limit:
            people.remove(x)
            people.remove(y)
            answer += 1
        
        else:
            people.remove(y)
            answer += 1
            
    return answer


# 성공한 코드 (deque 활용)
from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()
    people = deque(people)
    
    while people:
        
        if len(people) == 1:
            answer += 1
            break
            
        if people[0] + people[-1] <= limit:
            people.popleft()
            people.pop()
            answer += 1
        
        else:
            people.pop()
            answer += 1
            
    return answer

# 성공한 코드 (투포인터 사용)
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    
    a = 0
    b = len(people) - 1
    
    while a < b:
        
        if people[a] + people[b] <= limit:
            a += 1
            answer += 1
        
        b -= 1
            
    return len(people) - answer