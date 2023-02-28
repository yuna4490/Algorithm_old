import sys
input = sys.stdin.readline

c = int(input()) # 테스트 케이스 개수

def backtracking(cnt):
    global result

    if cnt == 11:
        result = max(result, sum(check))
        return
    
    for i in range(11):
        if visited[i] or not powers[cnt][i]:
            continue
        visited[i] = 1
        check[i] = powers[cnt][i]
        backtracking(cnt + 1)
        visited[i] = 0
        check[i] = 0

for _ in range(c):
    
    powers = [list(map(int, input().split())) for _ in range(11)]

    check = [0 for _ in range(11)] # 포지션 체크
    visited = [0 for _ in range(11)] # 선수 방문 체크
    result = 0
    
    backtracking(0)
    print(result)