import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
powers = [list(map(int, input().split())) for _ in range(n)]
result = 1e9
s = []

def backtracking(k, v):
    global result
    if k == n//2:
        start = 0
        for comb in combinations(s, 2):
            start += powers[comb[0]][comb[1]]
            start += powers[comb[1]][comb[0]]
        
        link = 0
        arr = []
        for i in range(n):
            if i not in s:
                arr.append(i)
        
        for comb in combinations(arr, 2):
            link += powers[comb[0]][comb[1]]
            link += powers[comb[1]][comb[0]]

        result = min(result, abs(start-link))    
        return

    for i in range(v, n):
        if i not in s:
            s.append(i)
            backtracking(k+1, i+1)
            s.pop()

backtracking(0, 0)
print(result)