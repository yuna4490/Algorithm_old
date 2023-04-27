# 시간초과
def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        
        if cnt > limit:
            answer += power
        
        else:
            answer += cnt
            
    return answer

# 시간초과 해결 (제곱근 사용, if 조건 추가)
def solution(number, limit, power):
    answer = 1
    
    for i in range(2, number+1):
        cnt = 0
        for j in range(1, int(i**0.5+1)):
            if i % j == 0:
                cnt += 1
                
                if j ** 2 != i:
                    cnt += 1
        
        if cnt > limit:
            answer += power
        
        else:
            answer += cnt
            
    return answer