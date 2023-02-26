# 플로이드 워셜
# set 이용
# 다시 도전해볼 것

def solution(n, results):
    answer = 0
    
    ranks = [[0 for _ in range(n)] for _ in range(n)]
    
    for i, j in results:
        ranks[i-1][j-1] = 1 # 이긴 놈들은 1
        ranks[j-1][i-1] = -1 # 진 놈들은 -1
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if ranks[i][j] == 0:
                    # a가 b를 이기고 b가 c를 이기면 a는 c도 이긴 것
                    if ranks[i][k] == 1 and ranks[k][j] == 1:
                        ranks[i][j] = 1
                    
                    # a가 b한테 지고 b가 c한테 지면 a는 c한테도 진 것
                    elif ranks[i][k] == -1 and ranks[k][j] == -1:
                        ranks[i][j] = -1
    
    # 0이 하나인 애들만 셈. why? 
    # ranks[1][1], ranks[2][2]와 같이 자기 자신과의 승패는 0일 것이고 다른 애들과의 승패가 모두 정해졌다면 이 0의 개수는 한 개일 것이기 때문이다.
    
    for rank in ranks:
        if rank.count(0) == 1:
            answer += 1
            
    return answer