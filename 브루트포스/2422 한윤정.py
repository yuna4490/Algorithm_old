from itertools import combinations
n, m = map(int, input().split())

ice = [[0 for _ in range(n)] for _ in range(n)]

for i in range(m):
    x, y = map(int, input().split())
    ice[x-1][y-1] = 1
    ice[y-1][x-1] = 1

result = 0

for i in combinations(range(n), 3):
    if ice[i[0]][i[1]] or ice[i[0]][i[2]] or ice[i[1]][i[2]]:
        continue
    result += 1

print(result)