import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = list(map(str, input().split()))
alphabet.sort()
result = []

# 오름차순
# L 글자
# 최소 한 개의 모음, 두 개의 자음

def backtracking(start, cnt):
    if cnt == L:
        x = result.count('a') + result.count('e') + result.count('i') + result.count('o') + result.count('u')
        if x >= 1 and len(result) - x >= 2:
            print(*result, sep = '')
        return
    
    for i in range(start, len(alphabet)):
        if alphabet[i] not in result:
            result.append(alphabet[i])
            backtracking(i + 1, cnt + 1)
            result.pop()

backtracking(0, 0)
