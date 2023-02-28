import sys
input = sys.stdin.readline

c = int(input()) # 테스트 케이스 개수

def backtracking(cnt, sum):
    global result
    if cnt == 11:
        result = max(result, sum)
        return

    for i in range(11):
        # 이미 포지션이 있는 멤버이거나 해당 포지션의 능력치가 0일 때
        if members[i] or not powers[cnt][i]:
            continue

        members[i] = 1
        backtracking(cnt + 1, sum + powers[cnt][i])
        members[i] = 0

for _ in range(c):
    powers = [list(map(int, input().split())) for _ in range(11)]
    members = [0 for _ in range(11)] # 멤버 체크
    result = 0

    backtracking(0, 0)
    print(result)
