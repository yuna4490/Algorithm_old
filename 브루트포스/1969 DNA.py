n, m = map(int, input().split())

dna = [list(input()) for _ in range(n)]
result = ''
h = 0

for i in range(m):
    count = [0, 0, 0, 0] # A, C, G, T
    for j in range(n):
        if dna[j][i] == 'A':
            count[0] += 1
        
        elif dna[j][i] == 'C':
            count[1] += 1
        
        elif dna[j][i] == 'G':
            count[2] += 1
        
        else:
            count[3] += 1

    idx = count.index(max(count))

    if idx == 0:
        result += 'A'
        
    elif idx == 1:
        result += 'C'

    elif idx == 2:
        result += 'G'
        
    else:
        result += 'T'
        
    h += (n - max(count))

print(result)
print(h)