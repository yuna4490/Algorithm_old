# 더 효율적인 코드

def solution(N, stages):
    People = len(stages)
    faillist = {}
    for i in range(1, N + 1):
        if People != 0:
            faillist[i] = stages.count(i) / People
            People -= stages.count(i)
        else:
            faillist[i] = 0

    return sorted(faillist, key=lambda i: faillist[i], reverse=True)

# 내 코드
from collections import defaultdict

def solution(N, stages):
    
    result = []
    dic = defaultdict(int) # 클리어 X 플레이어 수만 저장
    
    for stage in stages:
        if stage > N:
            continue
            
        dic[stage] += 1
    
    for i in range(1, N+1):
        cnt = 0 # 도달한 플레이어 수
        for stage in stages:
            if stage >= i:
                cnt += 1
        
        if cnt != 0:
            dic[i] = dic[i] / cnt
        
        else:
            dic[i] = 0
    
    answer = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
    
    for x in answer:
        result.append(x[0])
    
    return result