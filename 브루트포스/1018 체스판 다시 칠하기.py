import sys
input = sys.stdin.readline

n, m = map(int, input().split())
case1 = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
case2 = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
chess = [input().rstrip() for _ in range(n)]
result = 64
for i in range(n-7):
    for j in range(m-7):
        cnt1 = 0 # 하얀색으로 바꿀 경우
        cnt2 = 0 # 검은색으로 바꿀 경우
        for a in range(i, i+8):
            for b in range(j, j+8):
                if chess[a][b] != case1[a-i][b-j]:
                    cnt1 += 1
                
                elif chess[a][b] != case2[a-i][b-j]:
                    cnt2 += 1

        result = min(result, cnt1, cnt2)

print(result)
