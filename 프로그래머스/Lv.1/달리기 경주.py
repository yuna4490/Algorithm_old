def solution(players, callings):
    
    idx = {i : player for i, player in enumerate(players)}
    p = {player : i for i, player in enumerate(players)}
    
    for calling in callings:
        rank = p[calling] # 현재 선수 랭킹
        tmp_p = idx[rank-1] # 현재 선수 이전 랭킹의 선수
        
        p[calling] -= 1
        p[tmp_p] += 1
        
        idx[rank] = tmp_p
        idx[rank-1] = calling
        

    return list(idx.values())