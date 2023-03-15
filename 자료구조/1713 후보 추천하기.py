import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

pictures = dict()
candidates = list(map(int, input().split()))

for i in range(k):
    if pictures.get(candidates[i]) == None:
        if len(pictures) < n:
            pictures[candidates[i]] = [1, i] 

        else:
            tmp = sorted(pictures.items(), key = lambda x: (x[1][0], x[1][1]))
            del pictures[tmp[0][0]] # 추천 수 제일 적고 오래된 애 지우기
            pictures[candidates[i]] = [1, i]
    
    else:
        pictures[candidates[i]][0] += 1

result = sorted(pictures.keys())
print(*result)


