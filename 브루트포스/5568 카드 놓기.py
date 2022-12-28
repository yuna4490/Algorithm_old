from itertools import permutations

n = int(input())
k = int(input())

cards = []
result = []
for _ in range(n):
    cards.append(input()) # str로 받음

for i in permutations(cards, k):
    result.append(''.join(i))

print(len(set(result)))

