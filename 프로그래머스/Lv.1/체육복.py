def solution(n, lost, reserve):
    
    reserve_tmp = set(reserve) - set(lost)
    lost_tmp = set(lost) - set(reserve)
    
    for i in reserve_tmp:
        if i-1 in lost_tmp:
            lost_tmp.remove(i-1)
        
        elif i+1 in lost_tmp:
            lost_tmp.remove(i+1)
    
    answer = n - len(lost_tmp)
    
    return answer