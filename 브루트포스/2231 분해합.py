n = int(input())

ans = 1000000
for i in range(1, n):
    tmp = list(str(i))
    c = i
    for j in tmp:
        c += int(j)
    
    if c == n:
        ans = min(ans, i)
        break

if ans == 1000000:
    ans = 0
print(ans)