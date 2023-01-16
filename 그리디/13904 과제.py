import sys
input = sys.stdin.readline

n = int(input())
hw = []
checked = [False] * 1001 #주의.. n까지라고 하면 안됨

for _ in range(n):
    d, w = map(int, input().split())
    hw.append((d, w))

hw = sorted(hw, key = lambda x: (x[1], x[0]), reverse=True)

result = 0
for i in range(n):
    d = hw[i][0]
    w = hw[i][1]
    for j in range(d-1,-1,-1):
        if not checked[j]:
            checked[j] = True
            result += w
            break

print(result)