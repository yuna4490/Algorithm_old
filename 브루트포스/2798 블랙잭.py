from itertools import permutations

n, m = map(int, input().split())
cards = list(map(int, input().split()))

ans = 0
for per in permutations(cards, 3):
    tmp = sum(per)
    if tmp <= m:
        ans = max(ans, tmp)

print(ans)